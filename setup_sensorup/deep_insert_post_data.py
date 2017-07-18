#!/usr/bin/env python3

DATASTREAM_TEMPLATE = \
"""
{ 
    "unitOfMeasurement": { 
        "name": "Occupancy", 
        "symbol": "occupied", 
        "definition": "##LINK##" 
    }, 
    "name": "Datastream_##NAME##", 
    "description": "##DESC##", 
    "observationType": "##LINK##", 
    "ObservedProperty": { 
        "name": "Property_##NAME##", 
        "definition": "##LINK##", 
        "description": "observedProperty for ##NAME##" 
    },
    "Sensor": { 
        "name": "Sensor_##NAME##", 
        "description": "##DESC##", 
        "encodingType": "application/pdf", 
        "metadata": "##DESC##" 
    } 
}
""".strip()

def createDatastreamString(name, link, desc):
    _seat = DATASTREAM_TEMPLATE
    _seat = _seat.replace("##NAME##", name)
    _seat = _seat.replace("##LINK##", link)
    _seat = _seat.replace("##DESC##", desc)
    return _seat

arrDS = []

_sleeping_pod = createDatastreamString(\
        "Sleeping Pod", \
        "https://en.wikipedia.org/wiki/Occupancy", \
        "Sleeping Pod")
arrDS.append(_sleeping_pod)

for i in range(10):
    _s = createDatastreamString(\
        "Seat_%d" % (i + 1), \
        "https://en.wikipedia.org/wiki/Occupancy", \
        "Seat_%d" % (i + 1))
    arrDS.append(_s)

_datastream_json = ",".join(arrDS)

with open("template.json", "r") as f:
    d = f.read()
d = d.replace("##NAME##",           "Jim")
d = d.replace("##DESCRIPTION##",    "hi")
d = d.replace("##PROPERTIES##",     "")
d = d.replace("##LOCATION_DESC##",  "Location desc")
d = d.replace("##LOCATION_NAME##",  "SMU")
d = d.replace("##COORDINATES##",    "1, 1")
d = d.replace("##DATASTREAMS##",    _datastream_json)

post_data = d 
# payload = {'some': 'data'}
# post_data = json.dumps(payload)
