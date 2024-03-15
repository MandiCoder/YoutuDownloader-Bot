from yt_dlp import YoutubeDL
from os.path import join


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
        
class PlayList():
    def __init__(self, sms, url:str) -> None:
        self.sms = sms
        self.url = url
        self.texto = "**🚚 --Descargando playlist:-- \n**"
        self.lista_videos = []
        self.count = 0
    
    def my_hook(self, d):        
        
        if d['status'] == 'downloading':
            if self.count == 0:
                mensaje = f"        **● Descargando: **`{d['info_dict']['title']}`\n"
                self.texto += mensaje
                self.sms.edit_text(self.texto)
            self.count +=1
        
        if d['status'] == 'finished':
            self.count = 0
            mensaje = self.texto.split("\n")
                
            if mensaje[-1] == '':
                mensaje.pop()
                
            mensaje[-1] = f"        ✓ **`{d['info_dict']['title']}`**\n"
            
            self.texto = "\n".join(mensaje)
            self.sms.edit_text(self.texto)       
            self.lista_videos.append({
                'file_path'    :    d['filename'],
                'title'        :    d['info_dict']['title'],
                'thumb'        :    d['info_dict']['thumbnails'][-1]['url'],
                'description'  :    d['info_dict']['description']
            })
            
    def download(self):
        ydl_opts = {
                'format': 'best',
                'outtmpl': join('downloads', '%(title)s.%(ext)s'),
                'logger': MyLogger(),
                'progress_hooks': [self.my_hook],
            }
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(self.url)
            self.sms.delete()
            return self.lista_videos
        
        