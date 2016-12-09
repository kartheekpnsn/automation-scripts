#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Used this script - to download posts from photographylife.com as PDF
import re
import urllib2
import urllib
import pdfkit # Additional module - sudo pip install pdfkit
# # Download and set path - http://download.gna.org/wkhtmltopdf/0.12/0.12.3.2/wkhtmltox-0.12.3.2_msvc2013-win32.exe
def download_pdf(url,file_name):
	try:
		pdfkit.from_url(url, 'Your-path-to-store-the-PDFs'+file_name+'.pdf')
	except Exception, why:
		print 'Failed:', why

url = urllib2.urlopen("https://photographylife.com/photography-tips-for-beginners")
data = url.read();

# Write your own pattern of hyper-link below
pattern = '<a href="https://photographylife.com/feed">RSS</a>.</p><h3>(.*)'+'<h3>Case Study series:'
m = re.search(pattern, data)

# Line below - finds all hyperlinks
links = re.findall('"((http|ftp)s?://.*?)"', m.group(1))
i = 1
for link in links:
	o_link = link[0]
	name = o_link[(len("https://photographylife.com/")):(len(o_link))]
	download_pdf(link[0],name)
	
