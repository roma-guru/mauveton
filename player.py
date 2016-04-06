import sys, os
from vk import get_audios,get_wall_audios,get_name,get_id

if sys.version_info[0] < 3:
    import codecs
    _open_func_bak = open # Make a back up, just in case
    open = codecs.open

def create_playlist_from_audios(owner_id, offset, token):
    playlist = "%s.m3u" % get_name(owner_id)
    info("Loading audios from VK")
    write_m3u(playlist, get_audios(get_id(owner_id), offset, 0, token))
    return playlist

def create_playlist_from_wall(owner_id, offset, token):
    playlist = "%s.m3u" % get_name(owner_id)
    info("Loading wall audios from VK")
    write_m3u(playlist, get_wall_audios(get_id(owner_id), offset, 500, token))
    return playlist

def write_m3u(playlist,audios):
    info("Writing m3u playlist")
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
    os.system("%s -@ \"%s\"" % (get_mpg123(),path) )

def play_file(path):
    os.system("%s \"%s\"" % (get_mpg123(),path) )

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

def get_home():
    if is_linux():
        return os.environ["HOME"]
    elif is_windows():
        return os.path.join(os.environ["HOMEDRIVE"], os.environ["HOMEPATH"])
    raise Exception("Unsupported platform")

def info(msg):
   print("\033[0;37;42m%s\033[0m" % msg)