import shutil, os

def takeBackup(image, outputPath = os.getcwd()):
	if not os.path.exists(outputPath + "/Backup"):
		os.makedirs(outputPath + "/Backup")
	shutil.copy(image, outputPath + "/Backup/")