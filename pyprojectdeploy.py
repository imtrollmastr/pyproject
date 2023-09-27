import webbrowser
import time
import pygame
import robloxpy
newcmdname = "lololololololmao1982318"
newcmdinstalled = "hdbfsiufgeyyuerytuv-___s"
isadmin = False
# auth
acc1 = ["imtrollmastr_","Jo Hang Johann LO","yomamaobama","admin"]
acc2 = ["sitypooh","Sze Yan Sity YEUNG","Aquarius1984!","officer"]
acc3 = ["guest","Johnny Appleseed","password","member"]
# main
print("WARNING: The program is currently only used for MacOS. Some things may not be compatible on other operating systems.")
print("1 - Create a temporary account")
print("2 - Sign in with an existing account")
authselection = input("Select a authentication method: ")
if authselection == "1":
    print("Unable to complete event/task (missing files)")
    print("ERROR CODE: 404")
elif authselection == "2":
    usrauth = input("Enter username: ")
    pswauth = input("Enter password: ")
    if usrauth == acc1[0] and pswauth == acc1[2] or usrauth == acc2[0] and pswauth == acc2[2] or usrauth == acc3[0] and pswauth == acc3[2]:
        print("Connecting to server...")
        time.sleep(3)
        print("Successfully connected to pyprojectserver.")
        time.sleep(1)
        print("Welcome to PyProject X")
        i = 0
        while i < 100:
            cmdbar = input(">")
            if cmdbar == "web deploy":
                webaddress = input("Enter URL: ")
                webbrowser.open(webaddress)
            elif cmdbar == "secret0940()":
                print("Connected to admin server.")
                isadmin = True
                identity = input("Enter identity: ")
            elif cmdbar == "wordrender deploy":
                print("English only, or the text will not show.")
                renderedword = input("Render: ")
                import pygame  
                pygame.init()  
                screen = pygame.display.set_mode((640, 480))  
                done = False  
  
                #load the fonts  
                font = pygame.font.SysFont("Gotham", 89)  
                # Render the text in new surface  
                text = font.render(renderedword, True, (158, 16, 16))  
                while not done:  
                    for event in pygame.event.get():  
                        if event.type == pygame.QUIT:  
                            done = True  
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  
                            done = True  
                    screen.fill((255, 255, 255))  
                    #We will discuss blit() in the next topic  
                    screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))  
  
                    pygame.display.flip()  
            elif cmdbar == "image deploy":
                import cv2
                import sys
                print("You must add the image into the uploads folder and put the name of the image in this input")
                imagename = input("Filename: ")
                img = cv2.imread("uploads/" + imagename, cv2.IMREAD_ANYCOLOR)
                while True:
                    cv2.imshow("umm idk",img)
                    cv2.waitKey(0)
                    sys.exit()
                cv2.destroyAllWindows()
            elif cmdbar == "video deploy":
                import cv2
                import numpy as np

                print("You must add the image into the uploads folder and put the name of the image in this input")
                filename = input("Filename: ")

                # Create a VideoCapture object and read from input file
                # If the input is the camera, pass 0 instead of the video file name
                cap = cv2.VideoCapture("uploads/" + filename)

                # Check if camera opened successfully
                if (cap.isOpened() == False):
                    print("Error opening video stream or file")

# Read until video is completed
                    while (cap.isOpened()):
    
    # Capture frame-by-frame
                        ret, frame = cap.read()
                    if ret == True:

        # Display the resulting frame
                        cv2.imshow('Frame', frame)

        # Press Q on keyboard to  exit
                        if cv2.waitKey(25) & 0xFF == ord('q'):
                            break

    # Break the loop
                    else:
                        break

# When everything done, release the video capture object
                cap.release()

# Closes all the frames
                cv2.destroyAllWindows()
            elif cmdbar == "getRBLX deploy_game":
                universeid = input("UniverseID: ")
                data = robloxpy.Game.External.GetUniverseData(universeid)
                print(data)
            elif cmdbar == "getRBLX help_game":
                print("BedWars by Easy.GG - 2619619496")
                print("Arsenal by RoLVE Community - 111958650")
                print("The Sack by Unknown - 5065095632")
                print("Please improve the help page by suggesting more UniverseIDs.")
            elif cmdbar == "getRBLX deploy_headshot":
                getplridfrominput = input("Enter player ID: ")
                webbrowser.open("https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds=" + getplridfrominput + "&size=48x48&format=Png&isCircular=false")
            elif cmdbar == "getRBLX deploy_playerdesc":
                plrid = input("Enter player ID: ")
                plrinfo = robloxpy.User.External.GetDescription(plrid)
                print("PlayerUserDesc: "+ plrinfo)
            elif cmdbar == "getRBLX help_playerdesc":
                print("imtrollmastr - 4216367898")
                print("lmanismyfriend - 4638997350")
                print("ewohio1 - 4940743705")
            elif cmdbar == "google deploy":
                query = input("Google Search: ")
                try:
                    from googlesearch import search
                except ImportError:
                    print("No module named 'google' found.")
                for j in search(query):
                    print(j)
            elif cmdbar == "playmusic":
                import os
                # warning: this only works on macos
                print("1 - Migraine by BoyWithUke")
                print("2 - Mixed Signals by Skrillex & Swae Lee")
                print("3 - Turn on the Lights again.. by Fred again.., Swedish House Mafia & Future")
                print("4 - Admit It (u don't want 2) by Fred again.. & I. JORDAN")
                print("5. C'est La Vie by Yung Gravy, bbno$, Rich Brian")
                print("6. You Need Jesus by BABY GRAVY, Yung Gravy, bbno$")
                musicselection = input("Music Number: ")
                if musicselection == "1":
                    os.system("afplay cdn/migrainefull.wav")
                elif musicselection == "2":
                    os.system("afplay cdn/mixedsignals.mp3")
                elif musicselection == "3":
                    os.system("afplay cdn/turnonthelightsagain.mp3")
                elif musicselection == "4":
                    os.system("afplay cdn/admitit.mp3")
                elif musicselection == "5":
                    os.system("afplay cdn/cestlavie.mp3")
                elif musicselection == "6":
                    os.system("afplay cdn/uneedjesus")
                else:
                    print("Enter a correct selection number or suggest a song at https://bit.ly/pyprojectsuggestions")
            elif cmdbar == "davinci-ai deploy":
                from openai2 import Chat
                api_key = "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"
                davinci = Chat(api_key=api_key, model="gpt-3.5-turbo-16k-0613")
                request = input("Talk to DaVinci: ")
                ans = davinci.request(request)
                print(ans)
            elif cmdbar == "word_render deploy_basic":
                renderedword_basic = input("Enter a word: ")
                print(renderedword_basic)
            elif cmdbar == "createcmds deploy":
                newcmdname = input("Input new command name: ")
                print("Variation 1: print(n)")
                print("Variation 2: webbrowser.open(n)")
                print("More variations coming soon.")
                variation = input("Enter variation number: ")
                if variation == "1":
                    printsomething = input("Enter variation value: ")
                elif variation == "2":
                    openpage = input("Enter variation value: ")
                else:
                    print("Enter valid variation.")
                print("Successfully created new command!")
            elif cmdbar == "installcmds deploy":
                print("Installation Directory:")
                print("1. >helloworld - prints 'hello world'")
                print("2. >youtube - Opens YouTube on command")
                selectinstallation = input("Enter installation number: ")
                if selectinstallation == "1":
                    print("Successfully installed >helloworld command.")
                    newcmdinstalled = "helloworld"
                elif selectinstallation == "2":
                    print("Successfully installed >helloworld command.")
                    newcmdinstalled = "youtube"
            elif cmdbar == newcmdname:
                if variation == "1":
                    print(printsomething)
                elif variation == "2":
                    webbrowser.open(openpage)
                else:
                    print("Unable to detect registered value.")
            elif cmdbar == newcmdinstalled:
                if newcmdinstalled == "helloworld":
                    print("hello world")
                elif newcmdinstalled == "youtube":
                    webbrowser.open("http://youtube.com/")

            else:
                if isadmin == False:
                    print("Enter a valid/registered command")
                elif isadmin == True:
                    print("Hello, administrator " + identity + ", please create a new registered command to continue.")
    else:
        print("Incorrect authentication login. Please restart and login again.")

else:
    print("Please restart and select a authentication method.")