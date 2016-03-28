import subprocess, time, sys, os
from vk import get_audios,download,get_name

def play_wall(owner_id, token):
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Bye! Listen to the good music & heal your soul...")

def create_playlist(owner_id, token):
    playlist = "%s.m3u" % get_name(owner_id)
    print("Loading playlist from VK")
    with open(playlist,"w") as f:
        for a in get_audios(owner_id, 0, 0, token):
            url = a["url"]
            url = url[:url.index("?")]

            artist = a["artist"]; title = a["title"]
            f.write("%s\n" % url)
    return playlist

def play_list(path):
    print("Starting playback")
    code=os.system("%s -@ \"%s\"" % (get_mpg123(),path) )
    print("ended with exit code %d" % code)

def play_file(path):
    #subprocess.call([get_mpg123(),path])
    a=os.system("%s \"%s\"" % (get_mpg123(),path) )
    print("ended with exit code %d" % a)

def is_linux():
    return sys.platform.startswith("linux")

def is_windows():
    return sys.platform.startswith("win") or sys.platform.startswith("cygwin")

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
        return os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"])
    raise Error("Unsupported platform")


base_dir = os.path.join(get_home(),"Music","Mauveton")