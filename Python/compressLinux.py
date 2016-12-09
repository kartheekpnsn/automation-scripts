#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # Requirements - sudo yum install tar or sudo apt-get install tar

import os
import sys

def errorMsg(compress = True, uncompress = True, addOn = ""):
	print "Send command line arguments in the below format"
	if addOn != "":
		print addOn
	if compress:
		print "For Compressing"
		print "python fileName.py --compress FOLDERNAME OUTPUT_ZIPNAME"
	if uncompress:
		print "For UnCompressing"
		print "python fileName.py --extract INPUT_ZIPNAME"
	sys.exit()

# # Run the main code
if __name__ == "__main__":
  # check for necessary arguments
	if len(sys.argv) < 3 or len(sys.argv) > 4:
		errorMsg(compress = True, uncompress = True)
	else:
		whatToDo = sys.argv[1]
		if whatToDo == "--compress": # for comperessing
			if len(sys.argv) != 4: # if it doesn't have all the required arguments
				errorMsg(compress = True, uncompress = False)
			# get the name to be stored
			name = sys.argv[3]
			# get the folder/file to be compressed
			folder = sys.argv[2]
			try:
				os.system('sudo tar --lzma -cvpf ' + name + '.tar.lzma ' + folder)
			except:
				print "Please Check whether the file exists"
		elif whatToDo == '--extract': # for uncompressing
			# get the name of the file
			name = sys.argv[2]
			# if has extension - leave as is
			if name.split(".")[-1] == "lzma":
				name = name
			else: # else add the extension
				name = name + ".tar.lzma"
			# uncompress
			try:
				os.system('sudo tar --lzma -xvf ' + name)
			except:
				print "Please Check whether the file exists"
		else:
			errorMsg(compress = True, uncompress = True)
