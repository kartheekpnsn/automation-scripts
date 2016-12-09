import os
from PIL import Image
##################################################################################
##################### To resize the Image and make thumbnails ####################
##################################################################################
def getThumbnails(image, outputPath = os.getcwd(), sizes = [[250, 250]]):
	if not os.path.exists(outputPath + "/Thumbnails"):
		os.makedirs(outputPath + "/Thumbnails")
	for size in sizes:
		img = Image.open(image)
		img.thumbnail(size)
		img.save(outputPath + "/Thumbnails/thumbnail_" + ".".join(image.split(".")[:-1]) + "_" +"_".join([str(i) for i in size]) + ".jpg")