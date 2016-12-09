import re
import time
import sys
import os.path
from sendMail import *


flag = True

filePath = 'fileName.txt'
errorFile = 'errorLog.txt'


while flag:
	f = open(filePath, 'r')
	data = f.read()
	f.close()

	if os.path.isfile(errorFile):
		f = open(errorFile, 'r')
		errorInfo = f.read()
		f.close()
	else:
		errorInfo = " "

	data = data.lower()
	allErrors = re.findall('error.*\n', data)
	allErrors = [i.replace('\n', '') for i in allErrors]
	
	newErrors = list(set(allErrors)-set(errorInfo.splitlines()))
	start = time.clock()
	if (len(allErrors)) > 0 and len(newErrors) > 0:
		if errorInfo == " ":
			errorInfo = "\n".join(newErrors)
		else:
			errorInfo = errorInfo + "\n".join(newErrors)
		f = open(errorFile, 'w')
		f.write(errorInfo + "\n")
		f.close()
		nowTime = time.strftime("%Y-%m-%d %H:%M")
		mail("kartheekpnsn@gmail.com", "New Error in log at " + nowTime, "\n".join(newErrors))
		# sys.exit()
	else:
		print "no errors at - " + time.strftime("%Y-%m-%d %H:%M")
		time.sleep(20)

