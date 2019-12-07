#!/usr/bin/env python3
import sys
import requests
import re
from bs4 import BeautifulSoup

#print("https://www.google.de/search?q=" + "+".join(sys.argv[1:]))

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
			try:
				s = soup.find_all("div", {"class": "answer"})[0]
				tdTags = s.find_all("div", {"class": "post-text"})
				for tag in tdTags:
					print(tag.text)
			except:
				print("i dont know :(")
				
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
