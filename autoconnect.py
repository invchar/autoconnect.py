#!/usr/bin/env python3.5
import os
import syslog
import time
import mechanicalsoup


def log(message):
    syslog.syslog(message)


def checkconnection():
	try:
		result = os.system("ping -c 1 google.com")
		if result == 0:
			log("autoconnect.py: Ping to Google successful")
			return True
		log("autoconnect.py: Ping to Google failed")
	except:
		log("autoconnect.py: Ping command failed")
    return False


def getconnected():
	try:
		browser = mechanicalsoup.StatefulBrowser()
		browser.open("http://www.capitol.state.tx.us")
		browser.follow_link("continue")
		log("autoconnect.py: Browser run complete")
	except Exception as e:
		log("autoconnect.py: Browser run failed")
		log(e)
		return False


def main():
	log("autoconnect.py: Modules imported")
	connected = checkconnection()
	if not connected:
		getconnected()


if __name__ == "__main__":
	main()

