#!/usr/bin/env python3

import sys
import requests
import re
from bs4 import BeautifulSoup

r = requests.get("https://www.google.de/search?q=" + "+".join(sys.argv[1:]))
soup = BeautifulSoup(r.text, "lxml")
s = soup.find("a", href=re.compile("https://stackoverflow"))

# Nothing found, appending "stackoverflow"
if s is None:
	r = requests.get("https://www.google.de/search?q=" + "+".join(sys.argv[1:]) + "+stackoverflow")
	soup = BeautifulSoup(r.text, "lxml")
	s = soup.find("a", href=re.compile("https://stackoverflow"))
	
# No results found
if s is None:
	print("i don't know :(")
	exit()

s = BeautifulSoup(requests.get(s["href"].split("url?q=")[1].split("&")[0]).text, "lxml")


accepted = s.find("div", {"class": "accepted-answer"})

if accepted is not None:
	t = accepted.find("div", {"class": "post-text"})

if accepted is None:
	t = s.find("div", {"class": "answer"})

# Apply Color highlighting
html = str(t).replace("<code>", "{{code}}").replace("</code>", "{{/code}}")
print (BeautifulSoup(html, "lxml").text.replace("{{code}}", '\n\033[92m').replace("{{/code}}", '\033[0m'))

