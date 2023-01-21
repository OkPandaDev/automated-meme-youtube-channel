import os

#clear the terminal

os.system("cls")

#ask user for video details

file = input("path to video: ")
title = input("title: ")
desc = input("description: ")
catagory = input("category (22 is defualt): ")
keywords = input("keywords (seperate by comma): ")
privacy = input("privacy status: ")

# run the upload command

os.system(f'python upload_video.py --file="{file}" --title="{title}" --description="{desc}" --category="{catagory}" --keywords="{keywords}" --privacyStatus="{privacy}"')