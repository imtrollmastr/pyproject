import webbrowser
import time
import pygame
import robloxpy
import getpass as gt
import sys
newcmdname = "lololololololmao1982318"
newcmdinstalled = "hdbfsiufgeyyuerytuv-___s"
isadmin = False
# parental settings
# please change parental preferences in authstore.py
import parentalsettings
if parentalsettings.requirepassword == True:
    parentpassword = input("Enter parental code: ")
    if parentpassword == parentalsettings.requiredpassword:
        pass
    else:
        print("Alerting parent.")
else:
    pass
        
# something
if isadmin == True:
    print("Stop hacking and changing variables.")
    quit()
else:
    pass
def error(code):
    print("Error Code " + str(code) + ":")
    if code == 400:
        print("Bad Request to Server.")
        quit()
    elif code == 401:
        print("Unauthorized.")
        quit()
    elif code == 402:
        print("Payment in order to continue.")
        quit()
    elif code == 403:
        print("Forbidden.")
        quit()
    elif code == 404:
        print("Not found.")
        quit()
    elif code == 405:
        print("Method not allowed.")
        quit()
    elif code == 406:
        print('Not acceptable.')
        quit()
    elif code == 407:
        print("Proxy authentication required.")
        quit()
    elif code == 408:
        print("Request timeout")
        quit()
    elif code == 409:
        print("Conflict.")
        quit()
    elif code == 410:
        print("Gone.")
        quit()
    elif code == 418:
        print("The requested entity body is short and stout.")
        print("Tip me over and pour me out.")
    elif code == 451:
        print("We're sorry, but PyProject has been blocked from your country/city.")
    else:
        print("Incorrect error code, please move on.")
        pass
# store usernames and passwords and authenticate them with json
import json
import os
import getpass as gt
user = gt.getuser()
import profilesys

# main
print("WARNING: The program is currently only used for MacOS. Some things may not be compatible on other operating systems.")
print("1 - Create a temporary account")
print("2 - Sign in with an existing account")
print("3 - Google Authentication")
authselection = input("Select a authentication method: ")
if authselection == "1":
    error(405)
elif authselection == "2":
    usrauth = input("Enter username: ")
    pswauth = input("Enter password: ")
    if usrauth == profilesys.x1["username"] and pswauth == profilesys.x1["password"] or usrauth == profilesys.x2["username"] and pswauth == profilesys.x2["password"] or usrauth == profilesys.x3["username"] and pswauth == profilesys.x3["password"] or usrauth == profilesys.x4["username"] and pswauth == profilesys.x4["password"] or usrauth == profilesys.x5["username"] and pswauth == profilesys.x5["password"] or usrauth == profilesys.x6["username"] and pswauth == profilesys.x6["password"] or usrauth == profilesys.x7["username"] and pswauth == profilesys.x7["password"] or usrauth == profilesys.x8["username"] and pswauth == profilesys.x8["password"]:
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
            elif cmdbar == "camcapture":
                import pygame
                import pygame.camera
                pygame.camera.init()
                camlist = pygame.camera.list_cameras()
                if camlist:
                    cam = pygame.camera.Camera(camlist[0], (1920, 1080))
                    cam.start()
                    image = cam.get_image()
                    print("Now in HD resolution!")
                    capname = input("Enter capture image name: ")
                    pygame.image.save(image, capname + ".png")
                    print("Please find the image in PyProject main directory.")
                else:
                    print("No camera device located.")
            elif cmdbar == "time deploy":
                from datetime import datetime
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print("Current time: " + current_time)
            elif cmdbar == "date deploy":
                from datetime import date
                today = date.today()
                print("Current date: " + str(today))
            elif cmdbar == "marketplace deploy":
                # Define a simple Product class
                class Product:
                    def __init__(self, name, price):
                        self.name = name
                        self.price = price

            # Create a list to store products
                products = []

            # Function to add a product to the marketplace
                def add_product():
                    name = input("Enter product name: ")
                    price = float(input("Enter product price: "))
                    product = Product(name, price)
                    products.append(product)
                    print(f"{name} added to the marketplace.")

# Function to display available products
                def display_products():
                    print("Available Products:")
                    for idx, product in enumerate(products, start=1):
                        print(f"{idx}. {product.name} - ${product.price:.2f}")

# Function to make a purchase
                def make_purchase():
                    display_products()
                    choice = int(input("Enter the number of the product you want to purchase: "))
    
                    if 1 <= choice <= len(products):
                        product = products[choice - 1]
                        print(f"You purchased {product.name} for ${product.price:.2f}.")
                    else:
                        print("Invalid choice.")

# Main loop
                while True:
                    print("\nMarketplace Menu:")
                    print("1. View Products")
                    print("2. Make a Purchase")
                    print("3. Exit")
                    if isadmin == True:
                        print("4. Add Product")
                    else:
                        pass

    
                    option = input("Enter your choice: ")
    
                    if option == '1':
                        display_products()
                    elif option == '2':
                        make_purchase()
                    elif option == '3':
                        print("Thank you for using the marketplace. Goodbye!")
                        break
                    elif option == "4":
                        if isadmin == True:
                            add_product()
                        else:
                            print("Invalid choice. Please try again.")
                    else:
                        print("Invalid choice. Please try again.")
    
            elif cmdbar == "weather deploy":
                # importing library
                import requests
                from bs4 import BeautifulSoup

# enter city name
                city = input("Enter city name: ")

# creating url and requests instance
                url = "https://www.google.com/search?q="+"weather"+city
                html = requests.get(url).content

# getting raw data
                soup = BeautifulSoup(html, 'html.parser')
                temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
                str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

# formatting data
                data = str.split('\n')
                time = data[0]
                sky = data[1]

# getting all div tag
                listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
                strd = listdiv[5].text

# getting other required data
                pos = strd.find('Wind')
                other_data = strd[pos:]

# printing all data
                print("Temperature: ", temp)
            elif cmdbar == "spotify deploy":
                import webbrowser
                print("WARNING: Only use this if you have Spotify installed.")
                print("1. Track")
                print("2. Playlist")
                print("3. Album")
                trackorplaylist = input("Track or Playlist: ")
                if trackorplaylist == "track":
                    track_id = input("Enter Track ID: ")
                    webbrowser.open("spotify:track:" + track_id)
                elif trackorplaylist == "playlist":
                    playlist_id = input("Enter Playlist ID: ")
                    webbrowser.open("spotify:playlist:" + playlist_id)
                elif trackorplaylist == "album":
                    album_id = input("Enter Album ID: ")
                    webbrowser.open("spotify:album:" + album_id)
                else:
                    print("Incorrect selection.")

            elif cmdbar == "getRBLX deploy_headshot(v2)":
                import requests
                user_id = input("Input User ID: ")
                url = "https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds=" + user_id +"&size=48x48&format=Png&isCircular=false"
                r = requests.get(url)
                if r.status_code == 200:
                    print(r.text)
                    copypasteimage = input("Copy and paste the imageUrl in here: ")
                    webbrowser.open(copypasteimage)
                else:
                    print("Input correct user ID.")
            elif cmdbar == "killterminal":
                killquery = input("Please confirm by entering your password: ")
                import profilesys
                if killquery == profilesys.x1["password"] or killquery == profilesys.x2["password"] or killquery == profilesys.x3["password"]:
                    print("Confirmed terminal kill. Thank you for using PyProject X")
                    quit()
                else:
                    print("Unable to kill due to failed authentication.")
            else:
                if isadmin == False:
                    print("Enter a valid/registered command")
                elif isadmin == True:
                    print("Hello, administrator " + identity + ", please create a new registered command to continue.")
    else:
        print("Incorrect authentication login. Please restart and login again.")
elif authselection == "3":
    import webbrowser

# Replace with your Google OAuth client ID, redirect URI, and desired scopes
    client_id = '1020918721284-90hmih7dghjusvud8kmbih0brn7m45fm.apps.googleusercontent.com'
    redirect_uri = 'https://pyproject-rho.vercel.app/callback.html/'
    scopes = ['openid', 'profile','email']  # Add the scopes you need

# Construct the Google OAuth2.0 authorization URL with scopes
    scope_str = ' '.join(scopes)
    auth_url = f'https://accounts.google.com/o/oauth2/auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope_str}'

# Open the authorization URL in the default web browser
    webbrowser.open(auth_url)
    time.sleep(4)
    print("Please restart and use the following authentication details:")
    print("Username: guest")
    print("Password: password")
else:
    print("Please restart and select a authentication method.")















