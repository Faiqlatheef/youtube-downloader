import youtube_dl
import urllib.request
from mutagen import File
from mutagen.id3 import APIC

# replace with the URL of the YouTube video
video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

# download the audio stream
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'audio.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'verbose': True
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

# download the video thumbnail
thumbnail_url = f'https://img.youtube.com/vi/{youtube_dl.utils.extract_id(video_url)}/maxresdefault.jpg'
thumbnail_path = 'thumbnail.jpg'
urllib.request.urlretrieve(thumbnail_url, thumbnail_path)

# set the album art for the audio file
audio_file = File('audio.mp3')
with open(thumbnail_path, 'rb') as f:
    audio_file.tags.add(
        APIC(
            encoding=3,
            mime='image/jpeg',
            type=3,
            desc=u'Cover',
            data=f.read()
        )
    )
audio_file.save()
