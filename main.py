from modules.pyrogram_init import PyrogramInit
from modules.downloads import download_video, download_audio
from modules.uploads import upload_video, upload_audio
from pyrogram.filters import command
from pyrogram import emoji

bot = PyrogramInit()

@bot.app.on_message(command("start"))
def start(app, m):
    m.reply(f"Hola {m.from_user.username}. bienvenido a mi Bot {emoji.FACE_WITH_TONGUE}")



@bot.app.on_message(command("get_video"))
def get_video(app, m):
    url = m.text.split(" ")[1]
    data = download_video(url, m)
    upload_video(app, m.chat.id, data)
    
    
    
@bot.app.on_message(command("get_audio"))
def get_audio(app, m):
    url = m.text.split(" ")[1]
    data = download_audio(url, m)
    
    upload_audio(app, m.chat.id, data)



bot.iniciar_bot()