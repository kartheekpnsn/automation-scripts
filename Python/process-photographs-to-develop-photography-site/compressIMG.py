from PIL import Image
import os
##################################################################################
##################### This is used to compress the image size ####################
##################################################################################
def compressIMG(image, outputPath = os.getcwd()):
	if not os.path.exists(outputPath + "/Compressed"):
		os.makedirs(outputPath + "/Compressed")
	img = Image.open(image)
	img.save(outputPath + "/Compressed/" + image, optimize=True, quality=95)