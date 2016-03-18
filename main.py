# -*- coding: utf-8 -*-
import sys,requests
import argparse

from player import play_wall, play_audios
if __name__ == "__main__":
    
    print(""" .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.
:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.
'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `""")
    print("♬·¯·♩¸¸♪·¯·♫¸·¯·♩¸¸♪·¯·♫ It's Mauveos ♛ Tone Time ♬·¯·♩¸¸♪·¯·♫¸·¯·♩¸¸♪·¯·♫¸")
    
    parser = argparse.ArgumentParser(description="Play VK music", prog='mauveos')
    parser.add_argument('-w','--wall', dest='wall_owner', type=int)
    parser.add_argument('-a','--audios', dest='audios_owner', type=int)
    ns = parser.parse_args()

    if 'wall_owner' in ns:
        vkid = ns.wall_owner
        play_wall(vkid)
    elif 'audios_owner' in ns:
        vkid = ns.audios_owner
        play_audios(vkid)