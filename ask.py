import sys
import requests
import re
from bs4 import BeautifulSoup

#print("https://stackoverflow.com/search?q=" + "+".join(sys.argv[1:]))

r = requests.get("https://stackoverflow.com/search?tab=votes&q=" + str(sys.argv[1]).replace("\"", ""))
soup = BeautifulSoup(r.text, "lxml")

s = soup.findAll('a', href=re.compile("^/questions/"))
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
