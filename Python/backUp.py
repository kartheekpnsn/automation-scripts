#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # To run - python backUp.py path-of-the-file-or-directory
# # # # All necessary Imports
import glob
import datetime
import shutil
import sys
import os
import time

backUpPath = "/home/ubuntu/" # Set a backup path
backUpPath = backUpPath + "BackUp" # Add a folder BackUp in the decided path

# # # # Create Necessary Directories
if not os.path.exists(backUpPath):
    os.makedirs(backUpPath)

if not os.path.exists(backUpPath + "/Logs"):
    os.makedirs(backUpPath + "/Logs")

def generateLogs(file_name, log_text):
    if not os.path.exists(backUpPath + "/Logs"):
        os.makedirs(backUpPath + "/Logs")
        os.chmod(backUpPath + "/Logs",stat.S_IRWXU)
    fo = open(backUpPath + "/Logs/" + file_name +".txt", "a")
    fo.write(log_text + "\n")

def backUp(files):
        for file in files:
            if os.path.exists(file):
            	if os.path.isfile(file):
                    shutil.copy(file, backUpPath + "/")
                    name = "".join(file.split("/")[-1].split(".")[ : -1])
                    ext = file.split("/")[-1].split(".")[-1]
                    os.rename(backUpPath + "/" + file.split("/")[-1], backUpPath + "/" + name + "-" + str(time.strftime('%Y-%m-%d-%H:%M:%S')) + "." + ext)
                    generateLogs("BackupLogs", "Backed up - " + str(file) + " on - " + str(time.strftime('%Y-%m-%d %H:%M:%S')))
                elif os.path.isdir(file):
                    name = file.split("/")[-1]
                    if name == "":
                    	name = file.split("/")[-2]
                    shutil.copytree(file, backUpPath + "/" + name + "-" + str(time.strftime('%Y-%m-%d-%H:%M:%S')))
                    generateLogs("BackupLogs", "Backed up - " + str(file) + " on - " + str(time.strftime('%Y-%m-%d %H:%M:%S')))
files = list()
if len(sys.argv) > 1:
	for i in xrange(1,len(sys.argv)):
		files.append(sys.argv[i])

backUp(files)
