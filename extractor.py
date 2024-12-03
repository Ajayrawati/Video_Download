import os
import json



def extract_format_data(format_data):
    extension = format_data["ext"]
    format_name = format_data["format"]
    url = format_data["url"]
    return {
        "extension" : extension,
        "format_name": format_name,
        "url" : url
    }



def extract_vedio_data_from_url(url):
    command = f'yt-dlp "{url}" -j'
    output = os.popen(command).read()
    vedio_data = json.loads(output)
    title = vedio_data["title"]
    formats = vedio_data["formats"]
    thumbnail = vedio_data["thumbnail"]
    formats = [extract_format_data(format_data) for format_data in formats]
    return {
        "title":title,
        "formats":formats,
        "thumbnail": thumbnail
    }