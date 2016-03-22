#Testing branches
import subprocess, time, sys, os
from vk import get_audios,download,get_name

def play_wall(owner_id, token):
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Bye! Listen to the good music & heal your soul...")

def play_audios(owner_id, token):
    try:
        for a in get_audios(owner_id, 0, 10, token):
            artist = a["artist"]; title = a["title"]
            print("Now playing: %s - %s"% (artist, title))
            path = get_path(get_name(owner_id), a)
            if not os.path.exists(path):
                download(a["url"], path)
            play_file(path)

    except KeyboardInterrupt:
        print("Bye! Listen to the good music & heal your soul...")

def play_file(path):
    subprocess.call([get_mpg123(),path])

def is_linux():
    return sys.platform.startswith("linux")

def is_windows():
    return sys.platform.startswith("win")

def get_mpg123():
    base = "mpg123"
    if is_linux():
        return os.path.join(base,"linux64","mpg123")
    elif is_windows():
        return os.path.join(base,"win32","mpg123.exe")

def get_path(owner, a):
    artist = a["artist"]
    title = a["title"]
    dir = os.path.join(base_dir, owner)
    if not os.path.exists(dir):
        os.makedirs(dir)
    return os.path.join(dir, "%s - %s.mp3" % (artist,title))

def get_home():
    if is_linux():
        return os.environ["HOME"]
    elif is_windows():
        return os.environ["HOMEPATH"]

base_dir = os.path.join(get_home(),"Music","Mauveton")