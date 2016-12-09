#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # Mainly useful for photographers - works only for DSLR Images

from PIL import Image, ImageDraw, ImageEnhance
import glob, os, shutil
from getProperties import getProperties
from getThumbnails import getThumbnails
from compressIMG import compressIMG
from addBlackBG import addBlackBG
from addWatermark import addWatermark
from takeBackup import takeBackup
from getHTML import getHTML
from moveWebsiteFolder import moveWebsiteFolder

def cleanUp(inputFolder, outputFolder, backupFolder):
	if inputFolder:
		shutil.rmtree(inputFolder)
	if outputFolder:
		shutil.rmtree(outputFolder)
		os.makedirs(outputFolder)
	if backup:
		shutil.rmtree(backup)



##################################################################################
################################ A.L.G.O.R.I.T.H.M ###############################
##################################################################################
# Step1: Fetch all images
# Step2: getProperties for each Image and store it in text file
# Step3a: Add black background to form thumbnails and place them in "Output/Edited" folder
# Step3b: getThumbnails for each Image and store it in "Output/Thumbnails" folder and delete all files with black background in "Output/Edited" folder
# Step4: Take backup
# Step5: Add watermark and save it with same name
# Step6: Compress images and save it with same name in "Output/Compressed" folder
# Step7: Generate html code
# Step8: Move the images to website path
# Step9: Clean images from the input, output, backup
# Step10: Clean all ".pyc" files

if __name__ == "__main__":
	# # # Main path for all folders and codes
	mainPath = "C:\Users\Kartheek\Desktop\For Photography"
	# # # Path for all your photos
	inputPath = mainPath + "\Input"
	# # # Path for all the images after processing to be stored
	outputPath = mainPath + "\Output"
	# # # Path for the website folder - where the final images are placed (thumbnails + originals)
	websitePath = "C:\Users\Kartheek\Desktop\Photography\mySnaps"


	# # Change the path to input
	os.chdir(inputPath)

	# # Step1: Fetch all images
	imagesList = glob.glob("*.jpg")

	# # Step2: getProperties for each Image
	imgProperties = [getProperties(eachImg) for eachImg in imagesList]

	# # Step3a: Add black background to form thumbnails and place them in "Output/Edited" folder
	[addBlackBG(eachImg, outputPath = outputPath) for eachImg in imagesList]

	# # Step3b: getThumbnails for each Image and store it in "Output/Thumbnails" folder and delete all files with black background in "Output/Edited" folder
	os.chdir(outputPath + "/Edited")
	blackBgImages = glob.glob("*.jpg")
	[getThumbnails(eachImg, outputPath = outputPath) for eachImg in blackBgImages]
	del blackBgImages
	os.chdir(inputPath)
	shutil.rmtree(outputPath + "/Edited")

	# # Step4: Take backup
	[takeBackup(eachImg, outputPath = mainPath) for eachImg in imagesList]

	# # Step5: Add watermark and save it with same name
	# ~ [addWatermark(eachImg, mainPath + "\Logo\MyLogoPNG.png") for eachImg in imagesList]

	# # Step6: Compress images and save it with same name in "Output/Compressed" folder
	[compressIMG(eachImg, outputPath = outputPath) for eachImg in imagesList]

	# # Step7: Generate html code
	getHTML(imgProperties, outputPath = outputPath)

	# # Step8: Move the images to website path
	moveWebsiteFolder(outputPath, websitePath)

	# # Step9: Clean images from the input, output, backup
	os.chdir(mainPath)
	cleanUp(inputFolder = False, outputFolder = outputPath, backupFolder = False) # mainPath + "/Backup")

	# # Step10: Clean all ".pyc" files
	pycs = glob.glob("*.pyc")
	[os.remove(eachPyc) for eachPyc in pycs]