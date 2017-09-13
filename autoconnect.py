#!/usr/bin/env python3.5
import os
import time
import mechanicalsoup

print("autoconnect.py: Modules imported")

def checkconnection():
	try:
		result = os.system("ping -c 1 google.com")
		if result == 0:
			print("autoconnect.py: Ping to Google successful")
			return True
		else:
			print("autoconnect.py: Ping to Google failed")
			return False
	except:
		print("autoconnect.py: Ping command failed")
		return False

def getconnected():
	try:
		browser = mechanicalsoup.StatefulBrowser()
		browser.open("http://www.capitol.state.tx.us")
		browser.follow_link("continue")
		print("autoconnect.py: Browser run complete")
	except:
		print("autoconnect.py: Browser run failed")
		return False

def main():
	connected = checkconnection()
	if not connected:
		getconnected()

if __name__ == "__main__":
	main()

