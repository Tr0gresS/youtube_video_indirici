import os
import urllib.error

import pytube
from pytube import Playlist

if os.name == "nt":
    ok = "İndirme Tamamlandı"

    path_1 = f"c:\\Users\\{os.environ['USERNAME']}\\Desktop"
    path_2 = f"c:\\Users\\{os.environ['USERNAME']}\\OneDrive\\Desktop"
    path_3 = f"c:\\Users\\{os.environ['USERNAME']}\\OneDrive\\Masaüstü"
    path_4 = f"c:\\Users\\{os.environ['USERNAME']}\\Masaüstü"
    if os.path.exists(path_1) == True:
        os.chdir(path_1)
    elif os.path.exists(path_2) == True:
        os.chdir(path_2)
    elif os.path.exists(path_3) == True:
        os.chdir(path_3)
    elif os.path.exists(path_4) == True:
        os.chdir(path_4)

    else:
        try:
            path = input("Videoları indirmek istediğiniz path  >> ")
            os.chdir(path)
        except FileNotFoundError:
            pass

    def mp4andmp3():
        sayac = 1
        url = input("Playlist url : ")
        usr_c = input("[1] Mp4 Formatında indir \n[2] Mp3 Formatında indir \n>> ")
        ply = Playlist(url)
        print("Bulunan Video Sayısı : ", len(ply.video_urls))


        if usr_c == "1":
            for i in ply.video_urls:
                pytube.YouTube(i).streams.filter(type="video",progressive=True,file_extension="mp4").order_by("resolution").desc().first().download()
                print(f"{sayac}. {pytube.YouTube(i).title}, {ok}")
                sayac += 1

        elif usr_c == "2":
            for i in ply.video_urls:
                pytube.YouTube(i).streams.filter(only_audio=True).first().download()
                print(f"{sayac}. {pytube.YouTube(i).title}, {ok}")
                sayac += 1



    def video():
        url = input("Video url : ")
        usr_c = input("[1] Mp4 Formatında indir \n[2] Mp3 Formatında indir \n>> ")
        print(f" {pytube.YouTube(url).title}, {ok}")


        if usr_c == "1":
            pytube.YouTube(url).streams.filter(type="video", progressive=True, file_extension="mp4").order_by("resolution").desc().first().download()
        elif usr_c == "2":
            pytube.YouTube(url).streams.filter(only_audio=True).first().download()



    while True:
        user_ = input("[1] Playlist indir\n[2] Video indir\n[3] Çıkış\nSeçiminiz --> ")
        if user_ == "1":
            try:
                mp4andmp3()
            except urllib.error.HTTPError:
                pass
        elif user_ == "2":
            try:
                video()
            except urllib.error.HTTPError:
                pass
        elif user_ == "3":
            break