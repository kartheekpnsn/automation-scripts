#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import urllib2
import sys
import time
import os
import glob
import os.path
import subprocess

def shutdownInitiate(text):
	os.chdir("YOUR-PHP/HTML-FILES-IN-APACHE-PATH-HERE")
	files = glob.glob("*_shutdown.html")
	flag = [os.remove(ind_file) for ind_file in files]
	f = open(str(time.strftime('%Y-%m-%d')) + '_shutdown.html', 'wb')
	f.write(text)
	f.close()	

def shutdownStart():
	try:
		# response = urllib2.urlopen("http://54.179.145.170/shutdown/"+ str(time.strftime('%Y-%m-%d')) + "_shutdown.html")
		response = urllib2.urlopen("YOUR-PATH-FOR-THE-WRITTEN-HTML-FILE"+ str(time.strftime('%Y-%m-%d')) + "_shutdown.html")
		comment = response.read()
		subprocess.call(["shutdown.exe", "/s", "/c", comment])
		sys.exit()
	except Exception, e:
		pass

def internet_on():
    try:
        response=urllib2.urlopen('https://www.google.com',timeout=1)
        return True
    except urllib2.URLError as err:
    	return False

if len(sys.argv) >= 2:
	text = " ".join(sys.arv[1:])
else:
	text = "Bye Bye, System is shutting down in a minute"
shutdownInitiate(text)
