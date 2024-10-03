import os
import pytube
import urllib.request
from mutagen import File
from mutagen.id3 import APIC
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC

# replace with the URL of the YouTube video
video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

# download the video and extract the audio stream
youtube = pytube.YouTube(video_url, use_oauth=True, allow_oauth_cache=True)
audio_streams = youtube.streams.filter(only_audio=True)
audio_stream = audio_streams.first()

# download the audio file
audio_path = audio_stream.download()

# download the video thumbnail
thumbnail_url = youtube.thumbnail_url
thumbnail_path = 'thumbnail.jpg'
urllib.request.urlretrieve(thumbnail_url, thumbnail_path)

# set the album art for the audio file
# Set album art
try:
    # Download thumbnail from YouTube
    thumbnail_url = youtube.thumbnail_url
    urllib.request.urlretrieve(thumbnail_url, "thumbnail.jpg")

    # Open audio file and set album art
    audio_file = MP3('audio.mp3', ID3=ID3)
    audio_file.tags.add(
        APIC(
            encoding=3,  # 3 is for utf-8
            mime='image/jpeg',  # image/jpeg or image/png
            type=3,  # 3 is for the cover image
            desc=u'Cover',
            data=open('thumbnail.jpg', 'rb').read()
        )
    )
    audio_file.save()
    print("Album art set successfully.")
except Exception as e:
    print("Error setting album art:", e)
# Clean up files
os.remove("thumbnail.jpg")
