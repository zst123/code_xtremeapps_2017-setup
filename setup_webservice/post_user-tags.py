#!/usr/bin/env python3

import requests, threading

skills = '''Essayist
Event planner
Fashion designer
Film critic
Film director
Fine artist
Flash developer
Flatter
Floral designer
Food stylist
Furniture designer
Game artist
Graphic designer
Hairstylist
Illustrator
Imagineer
Industrial designer
Interior designer
Jewellery designer
Journalist
Knitwear designer
Landscape Architect
Leadman
Limner
Luthier
Lyricist
Make-up artist
Marchand-mercier
Marine designer
Media designer
Model (art)
Multi-media artist
Muralist
'''.strip().split("\n")

def send(user, tag):
	post_url = 'https://codextremejimmyneutron.azurewebsites.net/webservice.asmx/createUserInterestTag'
	response = requests.post(post_url, data={'username': user, 'UserTag': tag })
	response_text = response.text
	if "true" in response_text:
		print "Done", user, "for", tag
	else:
		print "Error", user, "for", tag

for s in skills:
	t = threading.Thread(target=send, args = ("ibrahim", s))
	t.start()
