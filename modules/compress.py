from zipfile import ZipFile, ZIP_DEFLATED
from os.path import basename
from os import unlink
from pyrogram.types import Message
from wget import download
from PIL import Image

def compress_files(data:list, msg:Message):
    name_zip = data[0]["title"] + ".zip"
    text_send = "**🗄 Comprimiendo videos...**\n"
    sms = msg.reply_text(text_send)
    caption:str = ""
    thumb_full = download(data[0]["thumb"])
    imagen = Image.open(thumb_full)
    unlink(thumb_full)
    imagen_redimensionada = imagen.resize((320, 320))

    imagen_redimensionada.save('thumb.jpg')

    with ZipFile(name_zip, "w") as zip:
        count = 1
        for file in data:
            zip.write(
                filename=file["file_path"],
                arcname=basename(file["file_path"]),
                compresslevel=ZIP_DEFLATED
            )
            text_send += f"   ✓ **`{basename(file['file_path'])}`**\n"
            caption += f"**{count}- `{basename(file['file_path'])}`**\n"
            unlink(file["file_path"])
            sms.edit_text(text_send)
            count += 1
        sms.delete()

    sticker = msg.reply_sticker("AnimatedSticker.tgs")
    msg.reply_document(name_zip, caption=caption, thumb='thumb.jpg')
    sticker.delete()
    unlink("thumb.jpg")
    unlink(name_zip)

