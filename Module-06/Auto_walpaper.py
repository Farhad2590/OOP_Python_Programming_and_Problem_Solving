import requests
import json
import PyWallpaper

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# get the json
response = requests.get(api_url)
content = response.content.decode("UTF-8")


# convert string to json

dict_content = json.loads(content)
print (dict_content)

# get the image 

image_url = dict_content['url']
print("image_url")

# download the image
res = requests.get(image_url)

# save the image
with open('apod.png','wb') as image:
    image.write(res.content)

PyWallpaper.change_wallpaper('C:\Users\farha\OneDrive\Desktop\Python\OOP_Python_Programming_and_Problem_Solving\Module-06\apod.png')
