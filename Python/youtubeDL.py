#!/usr/bin/env python

# # for linux systems
# # usage: python youtubeDL.py "YOUR-PLAYLIST-URL"

# # # === NECESSARY IMPORTS === # # #
import os # for running youtube-dl
import sys # for exiting and command line arguments
import urllib2 # for scraping html code of url
import re # for matching and extracting title from url

# # # === FUNCTIONS === # # #
# # == downloadYT = function to download youtube using url (either playlist or video) == # #
# url = youtube playlist url or youtube video url
# title = title of the playlist (if playlist) so that a folder can be created
# flag = number of tries to download the video / playlist (max = 5, then exit)
# playlist = a bool flag saying whether the url is playlist or video
def downloadYT(url, title = None, flag = 0, playlist = True, defaultPath = "~"):
	os.chdir(defaultPath)
	try:
		if playlist:
			os.system("mkdir " + title)
			os.chdir(os.getcwd() + "/" + title)
		os.system('sudo youtube-dl -citk "' + url + '"')
	except:
		if flag == 5:
			print "Exceeded 5 re-tries"
			sys.exit()
		else:
			flag = flag + 1
			downloadYT(url = url, flag = flag)

# # == getTitle = function to get title by scraping the urls HTML Code == # #
# url = youtube playlist url or youtube video url
def getTitle(url):
	try:
		htmlCode = urllib2.urlopen(url).read()
		regex = re.compile('<title>(.*?)</title>', re.IGNORECASE|re.DOTALL)
		title = regex.search(htmlCode).group(1)
		title = "".join([i.strip().capitalize() for i in title.split()])
		# remove - Youtube
		title = title.split("-")[:-1]
	except:
		title = url.split("list=")[-1]
	return("".join(title))

# # == cleanText = function to clean text in the title of the playlist or video == # #
# text = title as text
def cleanText(text):
	text = text.replace('\n\n','\n')
	text = text.replace('\t',' ')
	text = '\n'.join([eachLine.strip() for eachLine in text.splitlines()])
	for ch in ['(', ')', '[', ']', '{', '}', '/', '\\', '%', '`', ';', '"', "'", '?', '<', '>']:
		if ch in text:
			text = text.replace(ch, '')
	return(text)

# # == isPlaylist = function that returns a bool value based on the url (whether it is a playlist or a video) == # #
# url = youtube playlist url or youtube video url
def isPlaylist(url):
	m = re.search('playlist', url)
	if m:
		return True
	else:
		return False


# # # === MAIN CLASS === # # #
if __name__ == '__main__':
	# read the value by command line argument
	ytURL = sys.argv[1]

	if ytURL != 'list': # if the value is not 'list' then it is a single video file or single playlist file
		playlist = isPlaylist(ytURL)
		title = getTitle(ytURL)
		title = cleanText(title)
		downloadYT(ytURL, title, flag = 0, playlist = playlist)
	else: # else it is a list of videos present in videos.txt
		f = open('videos.txt', 'r')
		links = f.read()
		links = [eachLink.strip() for eachLink in links.splitlines()]
		f.close()
		for eachLink in links:
			playlist = isPlaylist(eachLink)
			title = getTitle(eachLink)
			title = cleanText(title)
			downloadYT(eachLink, title, flag = 0, playlist = playlist)
