import datetime
import os
import sys
try:
	os.mkdir("code-logs")
except:
	pass

os.chdir("code-logs/")

# # Generate HTML Page
def genHTML(title, timestamp, body, files, urls, todo, filename):
	body = "..".join(body.splitlines())
	files = "\n".join(["<li>" + i + "</li>" for i in files])
	urls = "\n".join(["<li>" + i + "</li>" for i in urls])
	todo = "\n".join(["<li>" + i + "</li>" for i in todo])
	html = """<html>
	<head>
	<style type='text/css'>
	h1 {
	font-family: "Times New Roman";
	font-size: 36px;
	}
	.heading {
	font-family: "Times New Roman";
	font-size: 20px;
	font-weight: bold;
	}
	.content {
	font-family: "Times New Roman";
	font-size: 16px;
	}
	.body {
	position: relative;
	left: 160px;
	width: 70%;
	}
	hr {
	width: 70%;
	}
	</style>
	</head>
	<body>
	<center><h1>""" + title + """</h1></center>"""

	content = """<div class = 'body'>
	<p class = 'content'><span class = 'heading'>Time stamp: </span>""" + timestamp + """</p>
	<p class = 'content'><span class = 'heading'>Body: </span>""" + body + """ </p>
	<p class = 'content'><span class = 'heading'>Files: </span></p>
	<ul> """ + files + """
	</ul> 
	<p class = 'content'><span class = 'heading'>Links: </span></p>
	<ul> """ + urls + """
	</ul>
	<p class = 'content'><span class = 'heading'>To do:</span></p>
	<ol> """ + todo + """
	</ol>
	</div>
	<hr>
	"""

	if not os.path.isfile(filename):
		content = html + "\n" + content + "\n"
	else:
		f = open(filename, 'r')
		data = f.read()
		content = data + "\n" + content + "\n"
		f.close()
	f = open(filename, 'w')
	f.write(content)
	f.close()

# # Get current time stamp
now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")
time = now.strftime("%H_%M_%S")

# # Get the title, body, to-do list of what is updated
if os.path.isfile('body.txt'):
	f = open('body.txt', 'r')
	text = f.read()
	f.close()
	title = text.split("\n\n")[0].split(":")[1].strip()
	body = text.split("\n\n")[1].split(":")[1].strip()
	files = text.split("\n\n")[2].split(":")[1].strip().splitlines()
	urls = text.split("\n\n")[3].split(":")[1].strip().splitlines()
	todo = text.split("\n\n")[4].split(":")[1].strip().splitlines()
	filename = "_".join(title.split()) + ".html"
	genHTML(title = title, timestamp = date + " " + time.replace("_", ":"), body = body, files = files, urls = urls, todo = todo, filename = filename)
else:
	try:
		f = open('body.txt', 'w')
	except:
		f.close()
		f = open('body.txt', 'w')
	f.write("Title: Enter Title here\n\nBody: Update\n\nFiles:\nNone\n\nLinks:\nNone\n\nTo Do:\nNone\nNone")
	f.close()
	print "No body.txt file, Please fill something and come back"
	sys.exit()


