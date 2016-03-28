# -*- coding: utf-8 -*-
import sys,requests
import argparse

from player import play_wall, play_list, create_playlist
if __name__ == "__main__":
    
    print("""\033[0;32;40m .*-.      .-'.      .-@-.      .--.      .@-.      .--.      .*-.      .--.
\033[0;33;40m:::::.\033[0;32;40m\\\033[0;33;40m::::::::.\033[0;32;40m\\\033[0;33;40m::::::::.\033[0;32;40m\\\033[0;33;40m::::::::.\033[0;32;40m\\\033[0;33;40m::::::::.\033[0;32;40m\\\033[0;33;40m::::::::.\033[0;32;40m\\\033[0;33;40m::::::::.\033[0;32;40m\\\033[0;33;40m::::::::.
\033[0;32;40m'      `-*'      `.*'      `--'      `--'      `-@'      `-.'      `-*'      `\033[0m""")
    print("\033[1;37;40m♬·¯·♩¸¸♪·¯·♫¸·¯·♩¸¸♪·¯·♫ \033[1;35;40mIt's \033[1;36;40mMauveos \033[1;33;40m♛\033[1;36;40m Tone \033[1;35;40mTime \033[0;37;40m♬·¯·♩¸¸♪·¯·♫¸·¯·♩¸¸♪·¯·♫¸\033[0m\n")
    
    parser = argparse.ArgumentParser(description="Play VK music", prog='mauveton')
    parser.add_argument('-w','--wall', dest='wall_owner', type=int)
    parser.add_argument('-a','--audios', dest='audios_owner', type=int)
    parser.add_argument('-t','--token', dest='access_token', type=str)
    parser.add_argument('--noplay', dest='no_play', action='store_true')
    
    ns = parser.parse_args()

    if ns.wall_owner and ns.access_token:
        vkid = ns.wall_owner
        token = ns.access_token
        play_wall(vkid, token)
    elif ns.audios_owner and ns.access_token:
        vkid = ns.audios_owner
        token = ns.access_token
        playlist = create_playlist(vkid, token)
        if not ns.no_play:
            play_list(playlist)
    else:
        print("\033[0;37;41mNo Arguments!\033[0m")
        parser.print_usage()
