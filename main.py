# -*- coding: utf-8 -*-
import argparse

from player import play_list, create_playlist_from_wall, create_playlist_from_audios

def is_num(s):
    return s.replace('-','').isdigit()

if __name__ == "__main__":
    
    try: 
        print("\033[0;32;40m .\033[0;31;40m❉\033[0;32;40m-.      .-'.      .-\033[0;34;40m✿\033[0;32;40m-.      .--.      .\033[0;35;40m✿\033[0;32;40m-.      .--.      .\033[0;36;40m❁\033[0;32;40m-.      .--.")
        print("\033[0;33;40m:::::.\033[0;32;40m\\\033[0;33;40m::::::::.\033[0;32;40m\\\033[0;33;40m::::::::.\033[0;32;40m\\\033[0;33;40m::::::::.\033[0;32;40m\\\033[0;33;40m::::::::.\033[0;32;40m\\\033[0;33;40m::::::::.\033[0;32;40m\\\033[0;33;40m::::::::.\033[0;32;40m\\\033[0;33;40m::::::::.")
        print("\033[0;32;40m'      `-\033[0;33;40m✾\033[0;32;40m'      `.\033[0;35;40m✤\033[0;32;40m'      `--'      `--'      `-\033[0;31;40m✤\033[0;32;40m'      `-.'      `-\033[0;33;40m✤\033[0;32;40m'      `")
        print("\033[1;37;40m♬·¯·♩¸♫¸♪·¯·♫¸·¯·♩¸¸♪·¯·♫ \033[1;36;40mIt's Mauveos \033[1;33;40m♛\033[1;36;40m Tone Time \033[0;37;40m♬·¯·♩¸♫¸♪·¯·♫¸·¯·♩¸¸♪·¯·♫¸\n")
        print("\033[0m")
    except:
        print("\033[1;37;41mYour terminal sucks\033[0m - \033[1;37;40mNo fancy Unicode support =(\033[0m")
    
    parser = argparse.ArgumentParser(description="Play VK music from walls and audio lists of users/communities.", prog='mauveton')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-w','--wall', dest='wall_owner', type=str, help="user/group id to play audios from their wall")
    group.add_argument('-a','--audios', dest='audios_owner', type=str, help="user/group id to play their audios")
    parser.add_argument('-t','--token', dest='access_token', type=str, help="VK access token with audio permission", required=True)
    parser.add_argument('-o','--offset', dest='offset', type=int, help="Offset (# of audios for -a, # of posts for -w)", default=0)
    parser.add_argument('--noplay', dest='no_play', action='store_true', help="save playlist only, don't play it")
    
    ns = parser.parse_args()

    try:
        token = ns.access_token
        offset = ns.offset
        if ns.wall_owner and token:
            vkid = int(ns.wall_owner) if is_num(ns.wall_owner) else ns.wall_owner
            playlist = create_playlist_from_wall(vkid, offset, token)
            if not ns.no_play:
                play_list(playlist)
        elif ns.audios_owner and token:
            vkid = int(ns.audios_owner) if is_num(ns.audios_owner) else ns.audios_owner
            playlist = create_playlist_from_audios(vkid, offset, token)
            if not ns.no_play:
                play_list(playlist)
    except KeyboardInterrupt:
        print("\033[0;37;42mGood Bye! Listen to the good music..\033[0m")
