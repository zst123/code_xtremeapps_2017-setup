#!/usr/bin/env python3
import base64

url = "http://cxa2017-ws1.sensorup.com"

auth = "main:f09611ec-60f6-523b-8e74-96601912577b"
auth_encode = base64.b64encode(auth.encode()).decode("utf-8")
#auth_encode = 'bWFpbjpmMDk2MTFlYy02MGY2LTUyM2ItOGU3NC05NjYwMTkxMjU3N2I='