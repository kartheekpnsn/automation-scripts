from PIL import Image
from PIL.ExifTags import TAGS
# import os
# import glob

##################################################################################
############################# To get the Image Properties ########################
##################################################################################
def getProperties(img):
	ret = {}
	i = Image.open(img)
	info = i._getexif()
	for tag, value in info.items():
		decoded = TAGS.get(tag, tag)
		ret[decoded] = value
	# # How to format
	# format_string = "NIKON D800E + 35mm f/1.8 @ 35mm, ISO 100, f/11.0"
	# keys in dictionary Model + LensModel + " @ " + FocalLength + ISOSpeedRatings + FNumber + ExposureTime
	# example - 'Model': u'NIKON D5200', 'LensModel': u'70.0-300.0 mm f/4.0-5.6', 'FocalLength': (1300, 10), 'ISOSpeedRatings': 800, 'FNumber': (45, 10), 'ExposureTime': (1, 30)
	try:
		modelUsed = ret['Model']
		lensUsed = ret['LensModel']
		focalLength = str(ret['FocalLength'][0]/ret['FocalLength'][1]) + "mm"
		iso = "ISO " + str(ret['ISOSpeedRatings'])
		aperture = "f/" + str(ret['FNumber'][0]/float(ret['FNumber'][1]))
		exposureTime = str(ret['ExposureTime'][0]) + "/" + str(ret['ExposureTime'][1])

		format_string = modelUsed + " + " + lensUsed + " @ " + focalLength + ", " + iso + ", " + aperture + ", " + exposureTime
	except:
		format_string = "Edited using Adobe Photoshop CS6 and LightRoom"
	return format_string

# if __name__ == "__main__":
# 	inputPath = "C:\Users\Kartheek\Desktop\For Photography\Input"
# 	os.chdir(inputPath)
# 	imgList = glob.glob("*.jpg")
# 	for i in imgList:
# 		print i + " - " + getProperties(i)