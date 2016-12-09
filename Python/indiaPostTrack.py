#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # Code will work (99% of times) only in windows environment
# # Works only for this site - http://www.indiapost.gov.in/articleTracking.aspx
# # Requirements
# 1) PIL
# 2) SELENIUM
# 3) Tesseract.exe in windows

from PIL import ImageGrab
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# # The URL for india post to track the consignments
url = 'http://www.indiapost.gov.in/articleTracking.aspx'
your_consignment_id = "ENTER-YOUR-TRACKING-CONSIGNMENT-ID-HERE"

# # To clean the output of the OCR - Data of Captcha - map the characters to nearest possible digits
def cleanData(data):
	# ABCDEFGHIJKLMNOPQRSTUVWXYZ
	# abcdefghijklmnopqrstuvwxyz
	data = data.replace("B", "8")
	data = data.replace("D", "0")
	data = data.replace("I", "1")
	data = data.replace("J", "1")
	data = data.replace("L", "1")
	data = data.replace("O", "0")
	data = data.replace("Q", "0")
	data = data.replace("S", "5")
	data = data.replace("U", "4")
	data = data.replace("Z", "2")
	data = data.replace("a", "0")
	data = data.replace("b", "6")
	data = data.replace("i", "1")
	data = data.replace("j", "1")
	data = data.replace("l", "1")
	data = data.replace("o", "0")
	data = data.replace("s", "5")
	data = data.replace("u", "4")
	data = data.replace("z", "2")


driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()
inputElement = driver.find_element_by_id("TxtArticleNumber")
inputElement.send_keys(your_consignment_id)

# # Get a screenshot of the captcha - # # # "PLEASE ADJUST THE BELOW COORDINATES IF THE BELOW ONE ARE NOT WORKING"
im=ImageGrab.grab(bbox=(440,400,540,430)) # X1,Y1,X2,Y2
im.save('sample.jpg')
# # Run OCR on the captcha image saved (sample.jpg) and save it as sample.txt
# # Change your tesseract.exe path below
cmd = ["C:/Program Files/Tesseract-OCR/tesseract.exe", "sample.jpg", "sample"]
process = subprocess.Popen(cmd, stderr = subprocess.STDOUT, stdout=subprocess.PIPE)

time.sleep(10)
# # Read the captcha data from sample.txt
f = open('sample.txt', 'r')
data = f.read()
data = data.splitlines()[0].strip()
cleanData(data)
f.close()


# # Enter the captcha obtained the browser
inputElement = driver.find_element_by_id("txtCaptcha")
inputElement.send_keys(data)
try:
	# # Press submit (or ENTER KEY)
	inputElement.send_keys(Keys.ENTER)
except:
	pass

time.sleep(10)
im=ImageGrab.grab() # X1,Y1,X2,Y2
im.save('output.jpg')
