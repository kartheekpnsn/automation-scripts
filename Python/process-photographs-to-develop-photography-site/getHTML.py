import os, glob
def getHTML(picDetails, outputPath = os.getcwd()):
	# # HTML CODE for My site - instead of blahblah.jpg - original image, instead of blahblah2.jpg - my thumbnail image, instead of PicDetails - my SS,ISO,Aperture details are replaced
	text = """              <div class="4u">
	                <section class="box">
					  <a href="mySnaps/blahblah.jpg" class="image image-full" data-lightbox="image-1"><img src="mySnaps/Thumbnails/blahblah2.jpg" alt=""></a>
	                  <header>
	                    <h3>Caption</h3>
	                  </header>
	                  <p>PicDetails</p>
	                </section>
	              </div>"""

	os.chdir(outputPath + "/Compressed")
	original = glob.glob("*.jpg")
	os.chdir(outputPath + "/Thumbnails")
	thumbnails = glob.glob("*.jpg")

	# sort picDetails based on original
	picDetails = [x for (y,x) in sorted(zip(original, picDetails))]
	# sort thumbnails based on original
	thumbnails = [x for (y,x) in sorted(zip(original, thumbnails))]
	# finally sort original
	original.sort()

	count = 0
	while count < len(original):
		text2 = text.replace('blahblah.jpg', original[count])
		text2 = text2.replace('PicDetails', picDetails[count])
		text2 = text2.replace('blahblah2.jpg', thumbnails[count])
		if count % 3 ==0:
			print '            <div class="row">'
		print text2
		print "<!-- END HERE -->"
		count = count + 1
		if count % 3 ==0:
			if count != 0:
				print '            </div>'

