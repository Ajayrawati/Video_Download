from yt_dlp import YoutubeDL

# Function to list available formats
def list_formats(url):
    options = {
        'listformats': True,  # Show all available formats
    }
    with YoutubeDL(options) as ydl:
        ydl.download([url])

# Function to download video
def download_video(url, format_code, save_path):
    options = {
        'format': format_code,  # User-selected format
        'outtmpl': save_path    # Save location
    }
    with YoutubeDL(options) as ydl:
        ydl.download([url])

# Example usage:
video_url = input("Enter the video URL: ")
if video_url:
    print("Fetching available formats...")
    list_formats(video_url)

    format_code = input("Enter the format code to download: ")
    save_path = input("Enter the save path (e.g., video.mp4): ")
    download_video(video_url, format_code, save_path)
