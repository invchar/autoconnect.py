#!/usr/bin/env python3.5
import os
import time
import mechanicalsoup
from syslog import syslog, LOG_INFO, LOG_ERR


def log(log_level=LOG_INFO, message="No message provided"):
	syslog(log_level, message)


def checkconnection():
	try:
		result = os.system("ping -c 1 google.com")
		if result == 0:
			log(message="autoconnect.py: Ping to Google successful")
			return True
		log(LOG_ERR, "autoconnect.py: Ping to Google failed")
	except:
		log(LOG_ERR, "autoconnect.py: Ping command failed")
	return False


def getconnected():
	try:
		browser = mechanicalsoup.StatefulBrowser()
		browser.open("http://www.capitol.state.tx.us")
		browser.follow_link("continue")
		log(message="autoconnect.py: Browser run complete")
	except Exception as e:
		log(LOG_ERR, "autoconnect.py: Browser run failed")
		log(message=str(e))
		return False


def main():
	log(message="autoconnect.py: Modules imported")
	connected = checkconnection()
	if not connected:
		getconnected()


if __name__ == "__main__":
	main()

