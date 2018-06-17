import sys
import requests
import re
from bs4 import BeautifulSoup

#print("https://www.google.de/search?q=" + "+".join(sys.argv[1:]))

#old version
"""
r = requests.get("https://stackoverflow.com/search?tab=votes&q=" + str(sys.argv[1]).replace("\"", ""))
soup = BeautifulSoup(r.text, "lxml")

s = soup.findAll("a", href=re.compile("^/questions/"))
if len(s) == 1:
	print("i don't know :(")
else:
	r = requests.get("https://stackoverflow.com" + str(s[1].get("href")))

	soup = BeautifulSoup(r.text, "lxml")
	s = soup.find_all("div", {"class": "answer accepted-answer"})

	for tag in s:
		tdTags = tag.find_all("div", {"class": "post-text"})
		for tag in tdTags:
			print(tag.text)
"""

#new version
r = requests.get("https://www.google.de/search?q=" + "+".join(sys.argv[1:]))
soup = BeautifulSoup(r.text, "lxml")

s = soup.findAll("a", href=re.compile("https://stackoverflow"))

if len(s) == 0:
	r = requests.get("https://www.google.de/search?q=" + "+".join(sys.argv[1:]) + "+stackoverflow")
	soup = BeautifulSoup(r.text, "lxml")

	s = soup.findAll("a", href=re.compile("https://stackoverflow"))
	
	if len(s) == 0:
		print("i don't know :(")
		
	else:
		r = requests.get(str(s[0].get("href")).split("url?q=")[1].split("&")[0])

		soup = BeautifulSoup(r.text, "lxml")
		s = soup.find_all("div", {"class": "answer accepted-answer"})
		
		if len(s) == 0:
			s = soup.find_all("div", {"class": "answer"})[0]
			tdTags = s.find_all("div", {"class": "post-text"})
			for tag in tdTags:
				print(tag.text)
				
		else:
			for tag in s:
				tdTags = tag.find_all("div", {"class": "post-text"})
				for tag in tdTags:
					print(tag.text)
else:
	r = requests.get(str(s[0].get("href")).split("url?q=")[1].split("&")[0])

	soup = BeautifulSoup(r.text, "lxml")
	s = soup.find_all("div", {"class": "answer accepted-answer"})
	
	if len(s) == 0:
		s = soup.find_all("div", {"class": "answer"})[0]
		tdTags = s.find_all("div", {"class": "post-text"})
		for tag in tdTags:
			print(tag.text)
			
	else:
		for tag in s:
			tdTags = tag.find_all("div", {"class": "post-text"})
			for tag in tdTags:
				print(tag.text)