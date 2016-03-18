import subprocess, time, os
from vk import get_audios

def play_wall(id):
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Bye! Listen to the good music & heal your soul...")

def play_audios(id):
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Bye! Listen to the good music & heal your soul...")

def play_file(path):
	subprocess.call(get_mpg123(),path)
