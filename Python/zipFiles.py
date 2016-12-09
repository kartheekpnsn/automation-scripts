#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os
import glob
import zipfile

# os.chdir("C:\\Users\\ka294056\\Desktop\\new-receipts-2")
os.chdir("Choose the path to select the files")
# types = ("*.jpg",)
types = ("*.fileType1", "*.fileType2")
images = []
for files in types:
	images.extend(glob.glob(files))
sizes = list()
for i in images:
	sizes.append(float(os.path.getsize(i))/1000000)
# zip = list()
value = 0
temp = 0
temp2 = 0
for i in sizes:
	value = value + i
	temp = temp + 1
	if value >= 23:
		zip = zipfile.ZipFile('Images' + str(temp) + '.zip', 'a')
		for j in range(temp2, temp):
			zip.write(images[j])
		temp2 = temp
		zip.close()
		value = 0
zip = zipfile.ZipFile('Images' + str(temp) + '.zip', 'a')
for j in range(temp2, temp):
	zip.write(images[j])
