#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import glob, csv, xlwt, os
path = "PATH-TO-ALL-CSV-FILES"

os.chdir(path)
# create a work book
wb = xlwt.Workbook()
# # get all csv files using glob
for filename in glob.glob("*.csv"):
  # get file name with extension, file path
	(f_path, f_name) = os.path.split(filename)
	# get file name and its extension
	(f_short_name, f_extension) = os.path.splitext(f_name)
	# create a sheet with the file name
	ws = wb.add_sheet(f_short_name)
	# read the csv file
	spamReader = csv.reader(open(filename, 'rb'))
	# row by row and col by col write the csv back to excel
	for rowx, row in enumerate(spamReader):
		for colx, value in enumerate(row):
			ws.write(rowx, colx, value)
# save the final output to excel file
wb.save("combined.xlsx")
