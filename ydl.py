# Import the models

import os
from yt_dlp import YoutubeDL
import time



# Defining functions

#A function for animation

def animation(action):
    count = 3
    for i in range(count):
        for o in range(1,4):
            print(f"\r{action}"+ "."*o,end="",flush=True)
            time.sleep(0.5)
        print(f"\r{action}.   ", end="",flush=True)
    print("Executed")
    exit()
    
    
#Creating a function to call when we are downloading

def download(url,media_format):
    
    if media_format == "video":
        with YoutubeDL(video_options) as down:
            down.download([url])
    elif media_format == "audio":
        with YoutubeDL(audio_options) as down:
            down.download([url])
    elif media_format == "extract":
        with YoutubeDL(extract_options)as down:
            down.download([url])
    else:
        print("Option not found")
        exit()


# A function for creating space

def space():
    print("")

#--------------------ACTUAL-SYSTEM----------------------------------------------#

print("         Welcome to the Ydl. The best tool for youtube downloading      ")
space()



pwd = input("Would you like to know your current location [yes/no]: ").lower().strip()
space()


if pwd == "yes":
    print(os.getcwd())
    space()
    loc = os.getcwd()
    
    create = input("Would you like to create the 'yt-down'folder here [yes/no] ").lower().strip()
    space()
    
    if create == "yes":
        path = loc
    else:    
        path = input("Please type the path to the folder you want the output to be stored: ").strip()
        space()
        
else:
    path = input("Please type the path to the folder you want the output to be stored: ").strip()
    space()


#Creating the path

if not os.path.exists(path):
    print(f"{path} does not exist")
    animation("Close due to path error")
else:

    full_path = os.path.join(path, "yt-down")

    if not os.path.exists(full_path):
        os.makedirs(full_path)
        print(f"Your downloads will go to {full_path}")
        space()
    else:
        print("The folder 'yt-down' was already created")
        space()
        print(f"So now the path to the downloads is {full_path}")
        space()
        
#Obtaining Url 

url = input("Enter the url: ").strip()
space()

if not url:
    print("No Url was entered")
    space()
    animation("Exit")
    space()
    

media_format = input("""
               
What format will you like your video to be:
Video
Audio
Extract    [This is where the audio is extraced from your file]   
What is your choice: """).lower().strip()
space()

FORMAT_OPTIONS = {
    "video": "video",
    "audio": "audio",
    "extract": "extract"
}


if media_format not in FORMAT_OPTIONS:
    print("Invalid format selected.")
    print("Valid options are: video, audio, extract")
    exit()


#File Naming

choice = input("Do you want to use the default naming or you would like a custom naming [default/custom]: ").lower().strip()
space()

if choice == "default":
    output_name = "%(title)s"
else:
    output_name = input("What name would you like to give the file: ").strip()
    space()


#Options [How the file will be downloaded]

video_options = {
    "format": "bestvideo+bestaudio/best",
    "outtmpl": f"{full_path}/{output_name}.%(ext)s",
    "merge_output_format": "mp4",
    "quiet": True,
    "no_warnings": True,
}

audio_options = {
    "format": "bestaudio/best",
    "outtmpl": f"{full_path}/{output_name}.%(ext)s",
    "quiet": True,
    "no_warnings": True,
}

extract_options = {
    "format": "bestaudio/best",
    "outtmpl": f"{full_path}/{output_name}.%(ext)s",
    "quiet": True,
    "no_warnings": True,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}


print("📥 Downloading....")     

download(url,media_format)

print("Thank you for using 'ydl' ✅  ")
