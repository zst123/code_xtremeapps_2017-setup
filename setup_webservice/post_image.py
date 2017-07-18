#!/usr/bin/env python3
import requests
import base64
import uuid

with open("image.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

input = encoded_string
url = "https://codextremejimmyneutron.azurewebsites.net/webservice.asmx/addFloorPlanWithFacility"

id = str(uuid.uuid4()).split("-")[1]
print("ID:", id)
print("URL:", url)
dd={
    'floorPlanId': id,
    'picture': input,
}


res = requests.post(url, data= dd)
print(res.text)