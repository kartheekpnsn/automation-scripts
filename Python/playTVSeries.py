#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import subprocess
import os
import time

# # Create a text file (tv_series_log.txt) in the same director as this python file
# In the first line put the path
# In the second line put the name of the episode that you are currently watching (or the first episode of first season)
# Example:
# F:\Movies\ENGLISH\HIMYM
# How.I.Met.Your.Mother.S01E01.480p.5.1Ch.Web-DL.ReEnc-DeeJayAhmed.mkv


f = open('tv_series_log.txt', 'r')
data = f.read()
f.close()

url = data.splitlines()[0]
now_file = data.splitlines()[1]

movie_files = list()
for path, subdirs, files in os.walk(url):
	for name in files:
		# # Add all possible formats by "or" condition
		if os.path.join(path, name).split(".")[-1] == "mkv" or os.path.join(path, name).split(".")[-1] == "avi" or os.path.join(path, name).split(".")[-1] == "mp4":
			movie_files.append(os.path.join(path, name))

force_play = raw_input("Enter something (b for back episode, c for current episode, just enter for next episode: ")
if force_play == 'b':
	to_play = [movie_files[i-1] for i in xrange(len(movie_files)) if movie_files[i].split("\\")[-1] == now_file]
elif force_play !='':
	to_play = [i for i in movie_files if i.split("\\")[-1] == now_file]
else:
	to_play = [movie_files[i+1] for i in xrange(len(movie_files)) if movie_files[i].split("\\")[-1] == now_file]


os.remove('himym.txt')
f = open('himym.txt', 'w')
f.write(url + "\n" + to_play[0].split("\\")[-1])
f.close()

path_for_video_player = "PLACE-YOUR-PATH-FOR-VIDEO-PLAYER" # example: "C:/Program Files (x86)/VideoLAN/VLC/vlc.exe"
p = subprocess.Popen([path_for_video_player, to_play])
