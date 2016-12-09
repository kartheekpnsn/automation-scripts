#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Used this script - to download posts from photographylife.com as PDF
# # Download and set path - http://download.gna.org/wkhtmltopdf/0.12/0.12.3.2/wkhtmltox-0.12.3.2_msvc2013-win32.exe
import re
import urllib2
import urllib
import pdfkit # Additional module - sudo pip install pdfkit

# # To download the WEB POST as PDF
def download_pdf(url,file_name):
	try:
		pdfkit.from_url(url, 'Your-Path-to-store-PDFs' + file_name + '.pdf')
	except Exception, why:
		print 'Failed:', why

# # To check whether the URL Exists or not (fails when the posts ends)
def parseURL(flag, urlString):
	try:
		f = urllib2.urlopen(urlString)
		flag = 1
	except:
		flag = 0
	return(flag)

# # To get the post-name using TITLE Tag
def getPostName(urlString):
	url = urllib2.urlopen(urlString)
	data = url.read();
	pattern = '<title>(.*)'+'</title>'
	m = re.search(pattern, data)
	return(m.group(1))

# # To download the articles given the base url
def downloadArticles(base_url):
	count = 1
	flag = 1
	while 1:
		urlString = base_url + str(count)
		flag = parseURL(flag, urlString)
		if flag == 0:
			sys.exit()
		else:
			name = getPostName(urlString)
			download_pdf(urlString, name)

# Download What-if posts
downloadArticles("https://what-if.xkcd.com/")

# Download XKCD Comics
downloadArticles("http://xkcd.com/")
