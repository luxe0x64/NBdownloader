from pytubefix import YouTube
from os import system


#######################################################################################
#                          Created by: nobody3132 aka luxe0x64                        #
#                                      Date: 14.02.2025                               #
#                              Happy Saint Valentine's day!!!                         #
#                                       Version: 1.5                                  #
#######################################################################################


class TubeDownloader:

    def __init__(self):
        system('clear')
        self.link = None
        self.playList = None
    pass

    def Downloading(self):
        system('cat NBDownloader_banner.txt')
        self.playList = input("Playlist? \nY/n: ")
        if self.playList == "Yes" or self.playList == "yes" or self.playList == "y" or self.playList == "Y":
            self.link = input("link: ")
            try:
                YouTube(self.link).streams.first().download()
                print("Done.")
            except Exception as e:
                print("something went wrong...")
                print(e)
        else:
            self.link = input("link: ")
            try:
                YouTube(self.link).streams.first().download()
                print("done.")
            except Exception as  e:
                print("Something went wrong....")
                print(f"{e} ")
        print("Thanks for using. ")
    pass

youTubeDownloader = TubeDownloader()
youTubeDownloader.Downloading()
