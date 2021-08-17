'''
Date: 15-7-21
Author: Dhruva
'''
import os
# Gui
from GUI import main as gui, notFound, projectName, projectType
from GUI import search
from GUI import downloadYT
from GUI import options
# open Browser
import webbrowser

if __name__ == "__main__":
    while True:
        # print("YO")
        guiResp = gui()

        if "play music" in guiResp:
            songDir = os.path.join(os.getcwd(), "songs/")
            # print(os.listdir(songDir))
            songs = os.listdir(songDir)
            os.startfile(os.path.join(songDir, songs[0]))
            print("Playing Music")
        
        elif "search" in guiResp:
            searchResp = search()
            url = "https://www.google.com.tr/search?q={}".format(searchResp)
            webbrowser.open(url=url, new = 0)
        
        elif "download" in guiResp:
            url = downloadYT()
            option = options()

            # print("resp = ", url)
            exesDir = os.path.join(os.getcwd(), "exes/")
            exesDirContents = os.listdir(exesDir)
            # print(exesDirContents)

            for item in exesDirContents:
                if item.startswith("youtube-dl") and item.endswith("exe"):
                    if option == "Only Audio": 
                        os.system(f"{item} {url} -x ")
                    else:
                        os.system(f"{item} {url}")
                # print(item)

        elif "project" in guiResp:
            desktopDir = os.path.join(os.environ["HOMEPATH"], "Desktop")
            files = os.listdir(desktopDir)

            # Making Folder
            fileName = projectName()
            path = os.path.join(desktopDir, fileName)
            os.mkdir(path)
            # Opening Code
            os.system(f"cd {path} && code .")
            # print(fileName)
            
        else:
            print("Couldnt Find The Command")
            notFound(guiResp)