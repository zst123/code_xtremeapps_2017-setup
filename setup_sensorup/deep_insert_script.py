#!/usr/bin/env python3

import requests
import json
import re

from paramz import *
from deep_insert_post_data import *
from colours import *

headers = {
    'content-type': 'application/json',
    'Authorization': 'Basic ' + auth_encode
}

response = requests.post(url + "/v1.0/Things", data=post_data, headers=headers)
response_text = response.text
print(response_text)
print(" ")

jsonArray = json.loads(response_text)
datastreamLink = jsonArray["Datastreams@iot.navigationLink"]
print(datastreamLink)
print(" ")

response_text = requests.get(datastreamLink).text
datastreams = json.loads(response_text)['value']
idArray = []
for eachDatastream in datastreams:
	print("Name: " + eachDatastream['name'])
	id = str(eachDatastream['@iot.id'])
	print("Datastream ID: " + id)
	idArray.append(id)
	print("")

arduino_code = \
"""#define SERVER_IP %s
#define PORT 80
#define AUTH_ENCODED "Authorization: Basic %s"
#define DATASTREAM_ID_TEMP  %s""" % (url, auth_encode, idArray[0])

print("SUCCESS!")
print("")
print("Arduino code generated:")
cprint(YELLOW, arduino_code)

print("")
print("C# data stream array generated:")
#str_idArray = map(lambda x: '%d' % x, idArray)
cprint(YELLOW, "[ %s ]" % ', '.join(idArray))
print("")
print("")
