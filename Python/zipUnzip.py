#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Usage: python zipUnzip.py your-path-to-zip-or-unzip

# pip install zipfile
import zipfile
import os
import glob
import sys
import time

def unzipFiles(path):
	path = path.replace("\\","/") # Useful in windows paths
	os.chdir(path)
	types = ("*.zip", "*.rar")
	Zipfiles = []
	for files in types:
		Zipfiles.extend(glob.glob(files))
	print Zipfiles
	if len(Zipfiles) == 0:
		print "This Path("+path+") has no Zip Files"
		sys.exit()
	for files in Zipfiles:
		with zipfile.ZipFile(files, "r") as z:
			z.extractall(path)

def zipFiles(path):
	types = raw_input("Enter the file types seperated by space & all for every file").split()
	if types[0].lower() == "all":
		types = "*."
	else:
		types = ["*." + each_type for each_type in types]
	path = path.replace("\\","/") # Useful in windows paths
	os.chdir(path)
	Zipfiles = []
	for files in types:
		Zipfiles.extend(glob.glob(files))
	if len(Zipfiles) == 0:
		print "This Path("+path+") has no Files of your required type"
		sys.exit()
	zip = zipfile.ZipFile('Zip-'+ str(time.strftime('%Y-%m-%d(%H-%M-%S)')) +'.zip', 'a')
	for files in Zipfiles:
		zip.write(files)
	zip.close()

if len(sys.argv) >= 2:
	path = sys.argv[1:]
	# # For Unzipping
	[unzipFiles(each_path) for each_path in path]
	# # For Zipping
	[zipFiles(each_path) for each_path in path]
else:
	print "Error - Please Pass the path as Argument"
