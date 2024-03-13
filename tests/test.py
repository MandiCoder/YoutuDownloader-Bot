
from pytube import YouTube

url = "https://youtu.be/VsYzmYkeeP4?si=j8HMCEzdC7wEGYYw"



yt = YouTube(url, proxies={
    "http" : "35.185.196.38:3128"
})

title = yt.title

video = yt.streams.get_audio_only()
video.download(filename=f"{title}.mp3")