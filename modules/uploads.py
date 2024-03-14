from os import unlink
from requests import get
from PIL import Image
from moviepy.editor import VideoFileClip




def upload_video(app, message_id, data):
    file = data["file_path"]
    
    caption = f"**Nombre: __{data['title']}__\n\nDescripcion: __{data['description']}__**"
    sms = app.send_message(message_id, f"**🚀 Subiendo video: `{data['title']}`**")
    thumb = download_thumb(url=data['thumb'], name=data['title'])
    video = VideoFileClip(file)
    
    app.send_video(message_id, file, caption=caption, thumb=thumb, duration=video.duration)
    sms.delete()
    unlink(file)
    unlink(thumb)
    
    

    
def upload_audio(app, message_id, data):
    sms = app.send_message(message_id, f"**🚀 Subiendo audio: `{data['title']}`**")
    print("Subiendo audio")
    thumb = download_thumb(url=data['thumb'], name=data['title'])
    app.send_audio(message_id, data['file_path'], thumb=thumb)
    sms.delete()
    unlink(data["file_path"])
    unlink(thumb)
    
    
    
def download_thumb(url, name):
    img_name = f"{name}.jpg"    

    try:
        imagen = get(url)
        with open(img_name, 'wb') as img:
            img.write(imagen.content)
        
        imagen = Image.open(img_name)
        imagen.thumbnail((320, 320))
        imagen.save(img_name)
    except Exception as e:
        print(e)
        img_name = "Designer.png"
    
        
    
    return img_name