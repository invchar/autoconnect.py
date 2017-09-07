#!/usr/bin/env python
import os
import time
import mechanicalsoup

def checkconnection():
	try:
		result = os.system("ping -c 1 google.com")
		if result == 0:
			return True
		else:
			return False
	except:
		return False

def getconnected():
	try:
		browser = mechanicalsoup.StatefulBrowser()
		browser.open("http://google.com")
		browser.follow_link("continue")
	except:
		return False

def main():
	while True:
		connected = checkconnection()
		if not connected:
			getconnected()
		time.sleep(600)

if __name__ == "__main__":
	main()

