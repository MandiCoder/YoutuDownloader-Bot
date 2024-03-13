from os import unlink
from requests import get
from PIL import Image

def upload_video(app, message_id, data):
    caption = f"**Nombre: `{data['title']}`\n\nDescripcion: {data['description']}**"
    sms = app.send_message(message_id, f"**🚀 Subiendo video: {data['title']}**")
    thumb = download_thumb(url=data['thumb'], name=data['title'])
    app.send_video(message_id, data["file_path"], caption=caption, thumb=thumb)
    sms.delete()
    unlink(data["file_path"])
    unlink(thumb)
    
    
    
    
def upload_audio(app, message_id, data):
    sms = app.send_message(message_id, f"**🚀 Subiendo audio: {data['title']}**")
    print("Subiendo audio")
    thumb = download_thumb(url=data['thumb'], name=data['title'])
    app.send_audio(message_id, data['file_path'], thumb=thumb)
    sms.delete()
    unlink(data["file_path"])
    unlink(thumb)
    print(thumb)
    
    
    
def download_thumb(url, name):
    img_name = f"{name}.jpg"
    with open(img_name, 'wb') as img:
        img.write(get(url).content)
        
    imagen = Image.open(img_name)
    imagen.thumbnail((320, 320))
    imagen.save(img_name)
    return img_name