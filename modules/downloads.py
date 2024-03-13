from modules.progress import on_progress
from pytube import YouTube

output_directory = "downloads"

def download_video(url:str, message) -> dict:
    yt = YouTube(url, on_progress_callback=on_progress, proxies={"http" : "35.185.196.38:3128"})
    title = yt.title
    sms = message.reply(f"**🚚 Descargando video: `{title}`**")
    video = yt.streams.get_highest_resolution()
    file = video.download(output_path=output_directory)
    sms.delete()
  
    return {
        "title"         : title,
        "file_path"     : file,
        "thumb"         : yt.thumbnail_url,
        "description"   : yt.description
    }
    
    
    
def download_audio(url:str, message) -> dict:
    yt = YouTube(url, on_progress_callback=on_progress, proxies={"http" : "35.185.196.38:3128"})
    title = yt.title
    sms = message.reply(f"**🚚 Descargando audio: `{title}`**")
    video = yt.streams.get_audio_only()
    file = video.download(output_path=output_directory, filename=f"{title}.mp3")
    sms.delete()
  
    return {
        "title"         : title,
        "file_path"     : file,
        "thumb"         : yt.thumbnail_url,
    }