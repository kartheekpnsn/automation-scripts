#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # Randomizing a set of images as wallpapers for your desktop (This code adds a little bit of intelligence to the randomization)

# import ctypes to make the selected image as wallpaper
import ctypes
# imported random to use shuffle function for randomization
import random
# imported os to do file/path operations
import os
# imported operator to do the sorting on dictionaries by values
import operator

# # A constant value - not sure why we use it?!
SPI_SETDESKWALLPAPER = 20

# # Path for all the wallpapers
url = "PATH-FOR-YOUR-SET-OF-JPEG-IMAGES-TO-BE-SET-AS-WALLPAPERS"

# # Store all the images path in images list
images = list()
for path, subdirs, files in os.walk(url):
	for name in files:
		if os.path.join(path, name).split(".")[-1] == "jpg":
			images.append(os.path.join(path, name))

##################################################################################
###################### Making randomization more intelligent #####################
##################################################################################

# # If the wallpapers.txt not present - load with all images_path~score
if not os.path.isfile('wallpapers.txt'):
	f = open('wallpapers.txt', 'w')
	temp = [f.write(i + "~0\n") for i in images]
	f.close()

# # read the images and score from wallpapers.txt
f = open('wallpapers.txt', 'r')
readings = f.read()
# ~ shuffle the lines atleast to create some randomization and then join back into lines
readings = "\n".join(random.sample(readings.splitlines(), len(readings.splitlines())))
f.close()

# ~ read images path
images_from_readings = [i.split("~")[0] for i in readings.splitlines()]
# ~ read the scores
score_from_readings = [int(i.split("~")[-1]) for i in readings.splitlines()]

# # Add new images (that are not in the log - wallpapers.txt)
images_from_readings = images_from_readings + [i for i in images if i not in images_from_readings]
score_from_readings = score_from_readings + ([0]*len([i for i in images if i not in images_from_readings]))

# # Sort it based on scores
sorted_Image = [i for (j, i) in sorted(zip(score_from_readings, images_from_readings))]

# # Select the image with least score
image = sorted_Image[0]

# # Change wallpaper
try:
	ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image , 0)
except:
	pass

# # Increment the score by 1 for the selected image
score_from_readings[images_from_readings.index(image)] = score_from_readings[images_from_readings.index(image)] + 1

# # remove the existing wallpapers.txt to replace with new values
os.remove('wallpapers.txt')
# # replace the wallpapers.txt with new values and updated scores with updated image paths
f = open('wallpapers.txt', 'w')
temp = [f.write(i + "~" + str(j) + "\n") for i, j in zip(images_from_readings, score_from_readings)]
f.close()
