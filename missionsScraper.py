# Send a request to the server and check the response back
import requests 
# fetch the source code of the web page
from bs4 import BeautifulSoup

import os
from PIL import Image

def getDescription(soup):
	ps = soup.find_all("p")

	place = ""
	giver = ""
	level = ""

	description = ""

	for p in ps:
		strong = p.find_all('strong')

		for s in strong:
			if (s.string.lower() == "location"):
				place = s
				place = place.next_sibling.next_sibling.string.replace(" ", "").replace("-", ", ").replace(">", "").replace("Â", "")
				description += "You will find this quest in"+place+"."
								
			elif ("quest giver" in s.string.lower()):
				giver = s
				giver = giver.next_sibling.string.replace("Â", "")
				description += " Talk to"+giver+"."
			elif ("level" in s.string.lower()):
				level = s
				level = level.next_sibling.string.replace("Â", "")
				description += " Required"+level.lower()+"."

	return description


def sideQuests(url):
	info = []

	res = requests.get(url)

	soup = BeautifulSoup(res.text, 'html.parser')

	title = soup.find('h1')

	info.append(title.string+".")

	info.append('\n'+getDescription(soup))

	info.append("\nActions:")

	objectives = []
	objectives = soup.find_all('strong')

	for objective in objectives:
		if (objective.string == "Objectives:"):
			lis = objective.next_element.next_element.next_element
			i = 1
			for li in lis:
				if(li.string[0] != '\n'):
					info.append(str(i)+"."+li.string)
					i += 1

	return info

def getImage(imageUrl, num):
	res = requests.get(imageUrl)

	soup = BeautifulSoup(res.text, "html.parser")

	firstTitle = soup.find('h2')

	link = firstTitle.find_next('a').attrs.get("href")

	#src = link.attrs.get('src')

	with open('image_'+str(num)+'.jpg', 'wb') as f:
		res = requests.get(link)
		f.write(res.content)

	#image = Image.open('image.jpg')
	#image.show()


def legacyCbot():
	url2 = "https://www.powerpyx.com/hogwarts-legacy-all-side-quests-guide/"
	res2 = requests.get(url2)

	soup2 = BeautifulSoup(res2.text, 'html.parser')

	sidesTitles = []
	sidesTitles = soup2.find_all('h2')

	for sidesTitle in sidesTitles:
		if 'side' in sidesTitle.next_element.string.lower():
			links = []
			links = sidesTitle.find_next('ol').find_all('li')

			hrefCopy = ""
			i = 0

			for link in links:
				i += 1

				href = link.find_next('a').attrs.get("href")

				createTweetFile(i, sideQuests(href))
				getImage(href, i)


			if (href == hrefCopy):
				continue
		

			hrefCopy = href;
			break


def createTweetFile(num, tweet):
	fd = open("tweet_"+str(num), "w+")

	with fd as out:

		for line in tweet:
			out.write(line+'\n')

	fd.close()

legacyCbot()