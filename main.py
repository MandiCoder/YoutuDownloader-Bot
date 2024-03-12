from modules.pyrogram_init import PyrogramInit
from pyrogram.filters import create, command
from pyrogram import emoji
from pytube import YouTube

bot = PyrogramInit()

@bot.app.on_message(command("start"))
def start(app, m):
    m.reply(f"Hola {m.from_user.username}. bienvenido a mi Bot {emoji.FACE_WITH_TONGUE}")



@bot.app.on_message(create(lambda f, c, u: u.text.startswith("https://youtu")))
def get_url(app, m):
    yt = YouTube(m.text)
    print(yt.title)
    print(yt.thumbnail_url)
    print(yt.description)
    print(yt.metadata)

bot.iniciar_bot()