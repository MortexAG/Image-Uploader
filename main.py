import requests
import os
import PIL
import dotenv
from dotenv import load_dotenv

load_dotenv()

clientid = os.environ["clientid"]
clientsecret = os.environ["clientsecret"]
accesstoken = os.environ["accesstoken"]
def upload_image(imagepath, image_name):
    url = "https://api.imgur.com/3/upload"

    payload={}
    files=[
      ('image',(image_name,open(imagepath,'rb')))
    ]
    headers = {
      'Authorization': f'Bearer {accesstoken}'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    result = response.json()
    print(result)
    print(result["data"]["link"])
def get_image(image_id):
    url = f"https://api.imgur.com/3/image/{image_id}"

    payload={}
    headers = {
      'Authorization': f'Client-ID {clientid}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    result = response.json()
    print(result)
#get_image('')
#upload_image("test-image.png", "test-image.png")
