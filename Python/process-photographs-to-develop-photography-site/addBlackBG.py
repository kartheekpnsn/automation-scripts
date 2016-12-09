import os
from PIL import Image
##################################################################################
# This is used to form a black background and scale the image to 6000x6000 nearly 
##################################################################################
def addBlackBG(image, outputPath = os.getcwd()):
	if not os.path.exists(outputPath + "/Edited"):
		os.makedirs(outputPath + "/Edited")
	img = Image.open(image)
	"return a black-background-color image having the img in exact center"
	size = (max(img.size),)*2
	layer = Image.new('RGB', size, (0,0,0))
	layer.paste(img, tuple(map(lambda x:(x[0]-x[1])/2, zip(size, img.size))))
	square_one = layer
	square_one.resize((100, 100), Image.ANTIALIAS)
	square_one.save(outputPath + "/Edited/" + image[:-4] + "_edited.jpg")