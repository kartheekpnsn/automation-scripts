# MyScripts

Scripts to help with little automation in our life.

## Directory Structure

```
.
+-- install-openCV.sh 										
+-- useful Snippets.txt 									
+-- Python                     								
|   +-- process-photographs-to-develop-photography-site 	
|   +-- shutdown-your-computer-using-internet				
|   +-- addComments.py 										
|   +-- backUp.py 											
|   +-- blueDartTrack.py 									
|   +-- compressLinux.py 									
|   +-- copyFiles.py 										
|   +-- csv2excel.py 										
|   +-- csv2sql.py 											
|   +-- downloadTalkingMachines.py 							
|   +-- downloadWebPages.py 								
|   +-- downloadXKCD.py 									
|   +-- dropboxUD.py 										
|   +-- fbPagePost.py 										
|   +-- generateLogs.py 									
|   +-- indiaPostTrack.py 									
|   +-- makeWallpaper.py 									
|   +-- mySQLConnect.py 									
|   +-- notifyError.py 										
|   +-- playTVSeries.py 									
|   +-- removeDupWords.py 									
|   +-- sendMail.py 										
|   +-- sendSMS.py 											
|   +-- youtubeDL.py 										
|   +-- zipFiles.py 										
|   +-- zipUnzip.py 										
+-- README.md
```

- [`install-openCV.sh`](https://github.com/automation-scripts/blob/master/install-openCV.sh) #To install OpenCV in Ubuntu systems.

- [`useful Snippets.txt`](https://github.com/automation-scripts/blob/master/useful Snippets.txt): some snippets regularly used for linux, python, R.

- [`Python/addComments.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/addComments.py) - This script adds a shebang line(if there is no shebang line) and a header comment. The comment says - Owner of the Script is Kartheek Palepu.

- [`Python/backUp.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/backUp.py) - This script backs up files or an entire folder with the date concatenated in a Backup folder. The path of the files/folder needs to be sent as command line arguments

- [`Python/blueDartTrack.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/blueDartTrack.py) - This script reads the tracking ID from the user and scrapes the shipment details from the blueDart site and prints the current status.

- [`Python/compressLinux.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/compressLinux.py) - This script compresses a file or a folder into best compression ratio (using lzma compression technique).

- [`Python/copyFiles.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/copyFiles.py) - This script copies the files from memory card (path to be given) to a local folder (path to be given). If the file already exists it renames the file. [Mainly Useful for photographers].

- [`Python/csv2excel.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/csv2excel.py) - This script reads one or multiple csv files and generates excel file out of them.

- [`Python/csv2sql.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/csv2sql.py) - This script reads a csv file and pushes into a database table. Even simpler script is found [here](https://github.com/okfn/nerc-rod-tools/blob/master/csv2sql.py)

- [`Python/downloadTalkingMachines.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/downloadTalkingMachines.py) - This script scrapes through the site [thetalkingmachines.com](http://www.thetalkingmachines.com) and downloads all the episodes/seasons from that website (generally its all audio podcasts)

- [`Python/downloadWebPages.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/downloadWebPages.py) - This script goes through every blog post in **["photographylife.com"](http://www.photographylife.com)** and then downloads each post as PDF and stores in local disk.

- [`Python/downloadXKCD.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/downloadXKCD.py) - This script goes through every blog post (based on post numbers) in XKCD and What-If and then downloads each post as PDF and stores in local disk.

- [`Python/dropboxUD.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/dropboxUD.py) - This script uploads and downloads from the dropbox account. It uses the API provided by Dropbox.

- [`Python/fbPagePost.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/fbPagePost.py) - This script posts any status updates on a Facebook page. Requirement - Facebook page and an App (id, key) for that Facebook page.

- [`Python/generateLogs.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/generateLogs.py) - This script generates text logs just by calling the function with file_name and text and parameters.

- [`Python/indiaPostTrack.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/indiaPostTrack.py) - This script reads the tracking ID from the user and then scrapes the india post website to generate the current status from the website. (Additionally as the site has CAPTCHA protected it also tries to break the CAPTCHA by processing it)

- [`Python/makeWallpaper.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/makeWallpaper.py) - This script goes through a series of images in the specified folder and applies a selected image as the background. This process is automated by maintaining the count so that no image is repeated. (until all the images are exhausted)

- [`Python/mySQLConnect.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/mySQLConnect.py) - This script has some useful functions - to connect DB, to apply DML on DB, to fetch data from DB.

- [`Python/notifyError.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/notifyError.py) - This script reads the log file supplied as input and alerts when an error occurs [Mainly used for code deployment monitoring].

- [`Python/playTVSeries.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/playTVSeries.py) - This script reads the specified folder of your required TV Series and then plays them sequentially just by a click until all the episodes are exhausted. (Reduced the pain to go through all seasons and episodes and select the current episode)

- [`Python/removeDupWords.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/removeDupWords.py) - This script removes duplicate words in a string preserving new line characters.

- [`Python/sendMail.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/sendMail.py) - This script uses **"smtplib"** and sends email to a specified mail-id from your id (currently configured for gmail) with a Subject and a Message

- [`Python/sendSMS.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/sendSMS.py) - This script uses **"Twilio API"** and sends SMS (not working with Indian numbers)

- [`Python/youtubeDL.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/youtubeDL.py) - This script reads URL from argument or input file and downloads the list of videos from youtube/facebook.

- [`Python/zipFiles.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/zipFiles.py) - This script is usually used when we have to mail a set of large files (mail allows only max 25MB) **Example** - If a folder has 100 files of size 250MB, the script produces 10 zip files each of 25MB.

- [`Python/zipUnzip.py`](https://github.com/kartheekpnsn/automation-scripts/blob/master/zipUnzip.py) - This script needs an input path as command line argument - which unzips all available zips or rars or zips all the required file types.
