import glob
import pdfkit
import os
import sys

os.chdir("code-logs")

html_files = glob.glob("*.html")

if len(html_files) == 0:
	print "No HTML Files found !"
	sys.exit()

print html_files

def writePDF(file):
	name = file.split(".")[0] + ".pdf"
	print name
	pdfkit.from_file(file, name)

[writePDF(i) for i in html_files]
[os.remove(i) for i in html_files]