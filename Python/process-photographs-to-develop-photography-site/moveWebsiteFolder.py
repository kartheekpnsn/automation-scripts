import shutil, glob, os

def moveWebsiteFolder(inputFolder, outputFolder):
	# move originals
	os.chdir(inputFolder + "/Compressed")
	originals = glob.glob("*.jpg")
	[shutil.copy(eachImg, outputFolder) for eachImg in originals]
	# move thumbnails
	os.chdir(inputFolder + "/Thumbnails")
	thumbnails = glob.glob("*.jpg")
	[shutil.copy(eachImg, outputFolder + "/Thumbnails") for eachImg in thumbnails]