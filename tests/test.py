from os.path import join
from yt_dlp import YoutubeDL


url = "https://youtube.com/playlist?list=PLtrlW8JHicSKY_iL6jwKwgswROodeDbQj&si=onfJmov_h7RsNo1I"

lista_videos = []

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        
        lista_videos.append({
            'filename' : d['filename'],
            'title'    : d['info_dict']['title'],
            'thumb'    : d['info_dict']['thumbnails'][-1]['url']
        })
   
        
        

ydl_opts = {
    'format': 'best',
    'outtmpl': join('downloads', '%(title)s.%(ext)s'),
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

    
with YoutubeDL(ydl_opts) as ydl:
    ydl_opts = {
        'format': 'best',
        'outtmpl': join('downloads', '%(title)s.%(ext)s'),
        'progress_hooks': [my_hook],

    }
    
    ydl.download(url)   
    
print(lista_videos)