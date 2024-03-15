from yt_dlp import YoutubeDL
from os.path import join
from modules.playlist import PlayList

output_directory = "downloads"
lista_videos = []


   

# DESCARGAR VIDEO -------------------------------------------------------
def download_video(url:str, message) -> dict:
    sms = message.reply("**⏳ Cargando...**")
            
    
    if url.startswith("https://youtube.com/playlist?"):
        lista_videos = PlayList(sms, url).download()
        return lista_videos
            
    else:
        ydl_opts = {
            'format': 'best',
            'outtmpl': join('downloads', '%(title)s.%(ext)s'),
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)   
            file = ydl.prepare_filename(info_dict)
            thumb = info_dict['thumbnail'] 
            title = info_dict['title']
            try:
                description = info_dict['description']
            except Exception as e:
                description = " "
                print(e)
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
    
    
    
# DESCARGAR AUDIO -----------------------------------------------------------
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