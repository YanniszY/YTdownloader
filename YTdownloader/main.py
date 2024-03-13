# code by YanniszY
# YT downloader v1.0

import os
from pytube import YouTube
from colorama import *


print(Fore.RED + ''' 
 __     _________       _                     _                 _           
 \ \   / /__   __|     | |                   | |               | |          
  \ \_/ /   | |      __| | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
   \   /    | |     / _` |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
    | |     | |    | (_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
    |_|     |_|     \__,_|\___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                                            
 ''')
print(Style.RESET_ALL)


yt = input("ссылка на видео >>> ") #ссылка на видео.
yt = YouTube(yt)


print(Style.BRIGHT + "default path: downloads! \n" + Style.RESET_ALL)

path = input("path to save file >>> ")

with open('path.txt', 'w') as filepath:
    filepath.write("path")


def video_360p():
    print(yt.streams.filter(file_extension='mp4')) 
    stream = yt.streams.get_by_itag(18)
    stream.download()

def video_720p():
    print(yt.streams.filter(file_extension='mp4')) 
    stream = yt.streams.get_by_itag(22)
    stream.download()

def video_1080p():
    print(yt.streams.filter(file_extension='mp4')) 
    stream = yt.streams.get_by_itag(137)
    stream.download()


def audio_50kbps():
    yt.streams.filter(file_extension='mp4')
    stream = yt.streams.get_by_itag(249)
    stream.download()

def audio_70kbps():
    yt.streams.filter(file_extension='mp4')
    stream = yt.streams.get_by_itag(250)
    stream.download()

def audio_160kbps():
    yt.streams.filter(file_extension='mp4')
    stream = yt.streams.get_by_itag(251)
    stream.download()


print("в каком формате будем скачивать видео? \n")
print("(1) [video] \"mp4\"\n(2) [audio] \"webm\"")

format = int(input(">>> "))

if format == 1:
    print("в каком качестве будем скачивать видео?")
    print("(1) [360p]\n(2) [720p]\n(3) [1080p]")
    quality_video = int(input(">>> "))
    if quality_video == 1:
        video_360p

    if quality_video == 2:
        video_720p()

    if quality_video == 3:
        video_1080p()

else:
    print("в каком качестве будем скачивать аудио?")
    print("(1) [50kbps]\n(2) [70kbps]\n(3) [160kbps]")
    quality_audio = int(input(">>> "))
    if quality_audio == 1:
        audio_50kbps()

    if quality_audio == 2:
        audio_70kbps()

    if quality_audio == 3:
        audio_160kbps()

