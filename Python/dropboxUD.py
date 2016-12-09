#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Own1er5 - Kartheek Palepu          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# http://www.braingle.in/brainteasers/codes/caesar.php
# pip install zipfile
import zipfile
import dropbox
import os
import glob
import sys
import datetime
import time
import urllib2
import shutil

def basics(path):
	os.chdir(path)
	if not os.path.exists(path + "/Upload"):
		os.makedirs(path + "/Upload")
	if not os.path.exists(path + "/Download"):
		os.makedirs(path + "/Download")

def internet_on():
    try:
        response=urllib2.urlopen('https://www.google.com',timeout=1)
        return True
    except urllib2.URLError as err:
    	return False

def zipdir(path, newFolderName):
	os.chdir(path)
	fileName = newFolderName.upper() + '_BackUp-'+ str(time.strftime('%Y-%m-%d(%H-%M-%S)')) +'.zip'
	zipf = zipfile.ZipFile(fileName, 'w', zipfile.ZIP_DEFLATED)
	os.chdir(path + "\Upload")
	for root, dirs, files in os.walk("."):
		for filez in files:
			print filez
			zipf.write(os.path.join(root, filez))
	zipf.close()
	os.chdir(path)
	shutil.move(fileName, "Upload/")
	return(fileName)

def dropBoxAuth():
	# auth_token = 'fJkS6FpqmprPPPPPPPPy7WmAAcYWw34gKbnh6BMqqG7dh_wrD-1x1fgkUgnpwYZS'
  	auth_token = 'USE-YOUR-TOKEN-HERE'
	client = dropbox.client.DropboxClient(auth_token)
	return(client)

def removeFiles(path):
	shutil.rmtree(path + '/Upload')
	os.chdir(path)
	if not os.path.exists(path + "/Upload"):
		os.makedirs(path + "/Upload")

def uploadFiles(path, newFolderName):
	client = dropBoxAuth()
	fileName = zipdir(path, newFolderName)
	os.chdir(path + "\Upload")
	f = open(fileName, 'rb')
	try:
		response = client.put_file('/BackUp/' + fileName, f)
		print "uploaded successfully"
		f.close()
		# removeFiles(path)
	except Exception, e:
		print str(e)
		f.close()

def downloadFiles(downPath, sfileName):
	# Path to save the files
	downPath = downPath.replace("\\","/") # Useful in windows paths
	downPath = downPath + "/Download"
	os.chdir(downPath)
	client = dropBoxAuth()
	path = "/BackUp"
	files = client.search(path, sfileName)
	if len(files) == 0:
		print "No files for the date - " + sfileName
	for i in files:
		allFiles = i["path"].split("/")[-1]
		try:
			f, metadata = client.get_file_and_metadata(path + "/" + allFiles)
			out = open(allFiles, 'wb')
			out.write(f.read())
			out.close()
		except:
			print "Failed to download"
			sys.exit()
	print "All files downloaded in - '" + downPath + "' folder"


# # Path for the upload and download folder
path = "C:\Users\Kartheek\Desktop\New folder"
basics(path)
if internet_on():
	requirement = raw_input("Enter 'u' for upload and 'd' for download: ").strip()
	if requirement.lower() == 'u':
		newFolderName = raw_input("Enter a folder name to be named for the Uploaded files: ").strip()
		uploadFiles(path, newFolderName)
	else:
		sfileName = raw_input("Enter a date (format = 31/12/2015) or nearly matched name: ").strip()
		if len(sfileName.split("/")) > 1:
			try:
				sfileName = datetime.datetime.strptime(sfileName, '%d/%m/%Y').strftime('%Y-%m-%d')
			except Exception, e:
				print str(e)
				print "Date Format error !"
				sys.exit()
		else:
			sfileName = sfileName.upper()
		downloadFiles(path, sfileName)
else:
	print "No Internet connection - please try later !"
