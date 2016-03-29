import sys, os
from vk import get_audios,get_wall_audios,download,get_name

if sys.version_info[0] < 3:
    import codecs
    _open_func_bak = open # Make a back up, just in case
    open = codecs.open

def create_playlist_from_audios(owner_id, token):
    playlist = "%s.m3u" % get_name(owner_id)
    print("Loading audios from VK")
    write_m3u(playlist, get_audios(owner_id, 0, 0, token))
    return playlist

def create_playlist_from_wall(owner_id, token):
    playlist = "%s.m3u" % get_name(owner_id)
    print("Loading wall audios from VK")
    write_m3u(playlist, get_wall_audios(owner_id, 0, 500, token))
    return playlist

def write_m3u(playlist,audios):
    with open(playlist,"w",encoding="utf-8") as f:
        f.write("#EXTM3U\n\n")
        for a in audios:
            url = a["url"]
            url = url.replace("https","http")
            url = url[:url.index("?")] if "?" in url else url
            artist = a["artist"]; title = a["title"]
            duration = a["duration"]

            f.write("#EXTINF:%d, %s - %s\n" % (duration,artist,title))
            f.write("%s\n" % url)

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