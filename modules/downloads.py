from yt_dlp import YoutubeDL
from os.path import join

output_directory = "downloads"

def download_video(url:str, message) -> dict:
    ydl_opts = {
        'format': 'best',
        'outtmpl': join('downloads', '%(title)s.%(ext)s'),
    }
    
    sms = message.reply("**⏳ Cargando...**")
    
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)   
        file = ydl.prepare_filename(info_dict)
        thumb = info_dict['thumbnail'] 
        title = info_dict['title']
        description = info_dict['description']

    sms.edit_text(f"**🚚 Descargando video: `{title}`**")
    
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
        
    sms.delete()
  
    return {
        "title"         : title,
        "file_path"     : file,
        "thumb"         : thumb,
        "description"   : description
    }
    
    
    
def download_audio(url:str, message) -> dict:
    opciones = {
        'format': 'bestaudio/best',
        'extractaudio': True,  
        'audioformat': 'mp3',  
        'outtmpl': join('downloads', '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    sms = message.reply("**⏳ Cargando...**")
    
    with YoutubeDL(opciones) as ydl:
        info_dict = ydl.extract_info(url, download=False)   
        thumb = info_dict['thumbnail'] 
        title = info_dict['title']
        file = join("downloads", f"{title}.mp3")
    
    sms.edit_text(f"**🚚 Descargando audio: `{title}`**")
    
    with YoutubeDL(opciones) as ydl:
        ydl.download(url)
        
    sms.delete()
  
    return {
        "title"         : title,
        "file_path"     : file,
        "thumb"         : thumb,
    }