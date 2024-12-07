from yt_dlp import YoutubeDL

def list_formats(url):
    options = {
        'listformats': True,  
    }
    with YoutubeDL(options) as ydl:
        ydl.download([url])

def download_video(url, format_code, save_path):
    options = {
        'format': format_code,  
        'outtmpl': save_path  
    }
    with YoutubeDL(options) as ydl:
        ydl.download([url])

video_url = input("Enter the video URL: ")
if video_url:
    print("Fetching available formats...")
    list_formats(video_url)

    format_code = input("Enter the format code to download: ")
    save_path = input("Enter the save path (e.g., video.mp4): ")
    download_video(video_url, format_code, save_path)
