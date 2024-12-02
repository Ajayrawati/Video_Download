from flask import Flask, request, jsonify
from yt_dlp import YoutubeDL

app = Flask(__name__)

# Route to fetch available formats
@app.route('/formats', methods=['POST'])
def list_formats():
    url = request.json.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    
    try:
        options = {
            'quiet': True,  # Suppress console logs
        }
        with YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = [
                {"format_id": f['format_id'], "format_note": f['format_note'], "ext": f['ext']}
                for f in info['formats']
            ]
        return jsonify({"formats": formats})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to download video
@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    url = data.get('url')
    format_code = data.get('format_code')
    save_path = data.get('save_path', 'video.%(ext)s')  # Default save path
    
    if not url or not format_code:
        return jsonify({"error": "Missing URL or format code"}), 400
    
    try:
        options = {
            'format': format_code,
            'outtmpl': save_path,
        }
        with YoutubeDL(options) as ydl:
            ydl.download([url])
        return jsonify({"message": "Download successful", "path": save_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
