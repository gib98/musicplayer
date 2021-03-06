import urllib.request
import os
import glob
from pygame import *

def goto_ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
    os.chdir(d)
goto_ensure_dir('music/')
playlist = []
queue = 0

def download_audio(youtube_url_id):
    url_start = 'http://www.youtubeinmp3.com/fetch/?video=https://www.youtube.com/watch?v='
    url = url_start + youtube_url_id
    file_name = youtube_url_id + '.mp3'

    urllib.request.urlretrieve(url, file_name)

    return file_name


def dl():
    playlist.append(download_audio('http://www.youtube.com/watch?v=btNs5wxTJ2k'))
    playlist.append(download_audio('https://www.youtube.com/watch?v=ENXvZ9YRjbo'))

def add_song(file_name):
    playlist.append(file_name)

def play_next_song():
    global playlist
    global queue
    song_name=playlist[0]
    mixer.music.load(song_name)
    mixer.music.play()
    try:
        playlist.remove(song_name)
    except:
        pass
    mixer.music.set_endevent(USEREVENT+1)
    
        

def play_playlist():
    global queue
    play_next_song()
    
    while True:
        for act in event.get():
            if act.type == USEREVENT+1:
                if playlist == []:
                    break
                else:
                    play_next_song()
                
        
        
    


def clear():
    global queue
    global playlist
    for item in glob.glob('*'):
        os.remove(item)
    queue=0
    playlist = []


init()

mixer.init()
