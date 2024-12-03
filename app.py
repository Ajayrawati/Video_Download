from flask import Flask, render_template,request
from extractor import extract_vedio_data_from_url
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download",methods=["POST"])
def download():
    vedio_url = request.form.get("video_url")
    if not vedio_url:
        return "Error: No video URL provided.", 400
    vedio_data = extract_vedio_data_from_url(vedio_url)
    return render_template("download.html",vedio_data=vedio_data)

if __name__ == "__main__":
    app.run(debug=True)