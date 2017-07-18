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

def create_observation(id, value, time):
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

SQUAREWAVE = True
values = ['2017', '07', '07', '00', '00', '00']
myDateTime = datetime.datetime(*map(int, values)) + datetime.timedelta(milliseconds=1)

_id = 491367


previousValue = 0
choices = [0, 0, 1, 1, 1]
for days in range(7):
    cprint(YELLOW, ">>>>>(Day %d)<<<<<" % (days))
    myDateTime += datetime.timedelta(days=1)
    for hour in range(8, 18+1):
        previoustime = myDateTime + datetime.timedelta(hours=hour, minutes=random.randint(0, 59))
        nexttime = previoustime + datetime.timedelta(milliseconds=1)
        
        if hour == 18 or 0:
            nextValue = 0
        else:
            nextValue = random.choice(choices)
        
        cprint(RED, "(%d hr) Doing %d for %s" % (hour, nextValue, get_proper_iso_time(previoustime)))
        
        if SQUAREWAVE:
            create_observation(id=_id, value=previousValue, time=get_proper_iso_time(previoustime))
        create_observation(id=_id, value=nextValue, time=get_proper_iso_time(nexttime))

        previousValue = nextValue
