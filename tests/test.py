from yt_dlp import YoutubeDL

def descargar_video_y_extraer_imagen(url):
    ydl_opts = {
        'format': 'best',  # Descargar en el mejor formato disponible
        'writeinfojson': True,  # Escribir metadatos en un archivo .info.json
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)   
        print(info_dict)
        thumbnail_url = info_dict['thumbnail']  # Extraer el enlace de la imagen del video

    return thumbnail_url

# Usar la función
url_del_video = 'https://youtu.be/VsYzmYkeeP4?si=j8HMCEzdC7wEGYYw'  # Reemplaza esto con la URL de tu video
url_de_la_imagen = descargar_video_y_extraer_imagen(url_del_video)
print(f'La URL de la imagen del video es: {url_de_la_imagen}')
