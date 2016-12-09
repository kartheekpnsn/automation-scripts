#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import re
import urllib2

urlString = "http://www.thetalkingmachines.com/blog/"

# # # Scrape through the url
url = urllib2.urlopen(urlString)
data = url.read();

# # Pattern found in source code of thetalkingmachines.com where download links can be found
pattern = """data-url="(.*)"
     data-mime-type=""
     data-title="(.*)"
     data-author=""
     data-show-download="(.*)"
     data-design-style="minimal"
     data-duration-in-ms="(.*)"
     data-color-theme="light">"""

# # Search the pattern
m = re.findall(pattern, data)

# # Get details into respective variables
links = [i[0] for i in m]
titles = [i[1] for i in m]

# # Download function
def downloadFile(url, title):
	req2 = urllib2.Request(url)
	response = urllib2.urlopen(req2)

	#grab the data
	data = response.read()

	mp3Name = title + ".mp3"
	song = open(mp3Name, "wb")
	song.write(data)
	song.close()

# # Download each file
[downloadFile(i, j) for i,j in zip(links, titles)]
