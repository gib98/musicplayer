import urllib.request
import os
import asyncio
import glob
from pygame import mixer, event

def goto_ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
    os.chdir(d)


def download_audio(youtube_url):
    url_start = 'http://www.youtubeinmp3.com/fetch/?video='
    url = url_start + youtube_url
    file_name = youtube_url[youtube_url.index('=') + 1:] + '.mp3'

    urllib.request.urlretrieve(url, file_name)

    return file_name


def dl():
    playlist.append(download_audio('http://www.youtube.com/watch?v=btNs5wxTJ2k'))
    playlist.append(download_audio('https://www.youtube.com/watch?v=ENXvZ9YRjbo'))


def play_playlist():
    mixer.music.load(playlist[0])
    mixer.music.play()
    mixer.music.set_endevent(SONG_END)
    while True:
        for event in event.get():
            break
        break
        
        
    


def clear():
    for item in glob.glob('*'):
        os.remove(item)


goto_ensure_dir('music/')
playlist = []

mixer.init()
