#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import glob
import os
import shutil

curr = "C:\Users\ka294056\Desktop\PySamples"
dest = "C:\Users\ka294056\Desktop\PySamples\New Folder"
os.chdir(curr)
types = ('*.py', '*.txt')
images = []
for files in types:
	images.extend(glob.glob(files))

for i in images:
	count = 1
	if not os.path.exists(dest + "\\" + str(i)):
		shutil.copy(str(i), dest + "\\" + str(i))
	else:
		while 1:
			extension = i.split('.')[-1]
			file_name = i.split('.')[0]
			if not os.path.exists(dest + "\\" + file_name + "_" + str(count) + "." + extension):
				shutil.copy(str(i), dest + "\\" + file_name + "_" + str(count) + "." + extension)
				break;
			else:
				count = count + 1
