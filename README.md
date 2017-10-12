# autoconnect.py
Uses Mechanical Soup to automatically accept terms on a wifi's captive portal

This script is being used on a Raspberry Pi running Ubuntu MATE in order to connect a separate device to a free wifi with a captive portal,
where the separate device is unable to make this connection itself.

This script is intended to be scheduled using Cron. 

It will attempt to ping a Google server. If it is successful, it does nothing else.
If it is not successful, we assume that we're being blocked by the captive portal configuration on the wifi. 
In this case, we use Mechanical Soup to try to get to the captive portal page. The HTTP request is made to a Texas government website, 
but the exact site doesn't matter as we intend to be redirected to the captive portal page. 
Once on the captive portal page, Mechanical Soup follows the continue button link, which enters our device into the captive portal system to be allowed internet access.

This Internet connection can be shared out the ethernet port of the Pi using the GUI in Ubuntu MATE. The Pi's initial connection to the wifi is also made in the GUI. 

An example crontab entry is as follows:
0,5,10,15,20,25,30,35,40,45,50,55 * * * * python3.5 /usr/lib/autoconnect/autoconnect.py

This example entry will run the script every 5 minutes. 

The script will log messages to the syslog
