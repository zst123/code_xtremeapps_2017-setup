#!/usr/bin/env python3

import requests
import json
import re
import datetime
import random

from paramz import *
from colours import *

headers = {
    'content-type': 'application/json',
    'Authorization': 'Basic ' + auth_encode
}

def get_proper_iso_time(dd):
	return dd.isoformat()[:-3] + "Z"

def create_observation(id=491363, value=0, time="2017-07-10T20:11:36.008Z"):
	post_data = '''{
		"result": %.2f,
		"resultTime": "%s",
		"phenomenonTime": "%s" 
	}''' % (value, time, time)
	#print(post_data)

	post_url = url + "/v1.0/Datastreams(%d)/Observations" % id

	response = requests.post(post_url, data=post_data, headers=headers)
	response_text = response.text

	cprint(PINK, response_text)

#class datetime.timedelta([days,] [seconds,] [microseconds,] [milliseconds,] [minutes,] [hours,] [weeks])

SQUAREWAVE = False
myDateTime = datetime.datetime.now()
previousValue = 0
choices = list(range(10))
for min in range(1, 101):
	nextValue = random.choice(choices)
	_id = 491363
	
	previoustime = myDateTime + datetime.timedelta(minutes=min)
	nexttime = previoustime + datetime.timedelta(milliseconds=1)

	cprint(RED, "(%d) Doing %d for %s" % (min, nextValue, nexttime))
	
	if SQUAREWAVE:
		create_observation(id=_id, value=previousValue, time=get_proper_iso_time(previoustime))
	create_observation(id=_id, value=nextValue, time=get_proper_iso_time(nexttime))

	previousValue = nextValue