from modules.pyrogram_init import PyrogramInit
from modules.downloads import download_video, download_audio
from modules.uploads import upload_video, upload_audio
from modules.compress import compress_files
from pyrogram.filters import command, regex, sticker
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import emoji, Client
from os import unlink

bot = PyrogramInit()
url_user = {}


@bot.app.on_message(command("start"))
def start(app, m):
    m.reply(f"Hola {m.from_user.username}. bienvenido a mi Bot {emoji.FACE_WITH_TONGUE}")

@bot.app.on_message(sticker)
def download_sticker(app, m):
    file = m.download()
    m.reply_document(file, force_document=True)
    unlink(file)


@bot.app.on_message(command("get_video") | regex("youtu"))
def get_video(app: Client, m: Message):
    url:str
    if len(m.text.split(" ")) > 1:
        url = m.text.split(" ")[1]
    else:
        url = m.text
    if url.startswith("https://youtube.com/playlist?"):
        m.reply_text(
            text="**Como desea que se envien los videos?**",
            reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text="🎬 Cada video por separado", callback_data="split")],
                    [InlineKeyboardButton(text="📦 Todos en un archivo [.zip]", callback_data="all")]
                ])
            )
        url_user[m.from_user.id] = url
    else:
        data = download_video(url, m)
        upload_video(app, m.chat.id, data)
    


@bot.app.on_callback_query()
def callback(app, callback):
    msg:Message = callback.message
    url = url_user[callback.from_user.id]
    msg.delete()

    if callback.data == "split":
        data = download_video(url, msg)
        upload_video(app, msg.chat.id, data)
    elif callback.data == "all":
        data = download_video(url, msg)
        compress_files(data, msg)



@bot.app.on_message(command("get_audio"))
def get_audio(app, m):
    url = m.text.split(" ")[1]
    data = download_audio(url, m)
    upload_audio(app, m.chat.id, data)



bot.iniciar_bot()