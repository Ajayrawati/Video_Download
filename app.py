from flask import Flask, render_template, request
from extractor import extract_vedio_data_from_url  # Ensure this module works correctly and returns expected data.

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Ensure you have 'index.html' in the 'templates' folder.

@app.route("/download", methods=["POST"])
def download():
    video_url = request.form.get("video_url")
    
    if not video_url:
        return "Error: No video URL provided.", 400
    
    try:
        # Extract video data
        video_data = extract_vedio_data_from_url(video_url)
        title = video_data.get("title", "No Title Available")
        thumbnail = video_data.get("thumbnail", "")
        formats = video_data.get("formats", [])
        
        mp4_formats = [
            format for format in formats 
            if 'mp4' in format.get('extension', '') and '.m3u8' not in format.get('url', '')
        ]
        
        unique_resolutions = {}

        for video in mp4_formats:
            # Extract resolution from format_name (e.g., 144p, 240p)
            resolution = video['format_name'].split()[-1]
            if resolution not in unique_resolutions:
                # Add the resolution as a separate key
                unique_resolutions[resolution] = {
                    **video,  # Include the original video data
                    'format_name_label': resolution  # Add format_name_label with resolution (e.g., '144p')
                }

        # Extract the filtered list
        filtered_videos = list(unique_resolutions.values())

        # Pass data to the template
        return render_template(
            "download.html", 
            title=title, 
            thumbnail=thumbnail, 
            formats=filtered_videos
        )
    
    except Exception as e:
        # Handle errors and display them
        print(f"Error: {e}")
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
