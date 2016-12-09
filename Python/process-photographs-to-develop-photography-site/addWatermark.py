from PIL import Image, ImageDraw, ImageEnhance

# # # INITIALLY REDUCE OPACITY THEN ADD WATERMARK
def reduce_opacity(img, opacity):
    """Returns an image with reduced opacity."""
    assert opacity >= 0 and opacity <= 1
    # Make the image as an alpha layer (RGBA)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    else:
        img = img.copy()
    alpha = img.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    img.putalpha(alpha)
    return img


def addWatermark(main_image, water_mark, imageFlag = True):
    if imageFlag:
        water_mark_image(main_image, water_mark)
    else:
        water_mark_text(main_image, water_mark)


##################################################################################
############################## Add Logo as Watermark #############################
##################################################################################
def water_mark_image(main_image, water_mark):
    waterMark = Image.open(water_mark, 'r')
    mainImage = Image.open(main_image, 'r')
    if mainImage.mode != 'RGBA':
        mainImage = mainImage.convert('RGBA')
    img_w, img_h = waterMark.size
    # Rezies the watermark image into 70% of the image height and width
    waterMarkResize = (int(round(img_w * 0.7)), int(round(img_h * 0.7)))
    waterMark = waterMark.resize(waterMarkResize, Image.ANTIALIAS)
    bg_w, bg_h = mainImage.size
    # offset is the position of the watermark to be placed - 70% of width and 85% of height
    offset = (int(round(bg_w * 0.9)), int(round(bg_h * 0.9)))
    # make the opacity to 0.8%
    waterMark = reduce_opacity(waterMark, 0.8)
    # paste the watermark on the main image
    mainImage.paste(waterMark, offset, waterMark)
    # Save it as water_mark_imageName
    mainImage.save("".join(main_image.split(".")[:-1]) + ".jpg")

##################################################################################
############################## Add Text as Watermark #############################
##################################################################################
def water_mark_text(main_image, water_mark):
    # Open the main image
    main = Image.open(main_image)
    # Create a new image for the watermark with an alpha layer (RGBA)
    #  the same size as the original image
    watermark = Image.new("RGBA", main.size)
    # Get an ImageDraw object so we can draw on the image
    waterdraw = ImageDraw.ImageDraw(watermark, "RGBA")
    # Place the text at (10, 10) in the upper left corner. Text will be white.
    waterdraw.text((round(main.size[0]*0.8), round(main.size[1]*0.95)), water_mark)
    # Get the watermark image as grayscale and fade the image
    # See <http://www.pythonware.com/library/pil/handbook/image.htm#Image.point>
    #  for information on the point() function
    # Note that the second parameter we give to the min function determines
    #  how faded the image will be. That number is in the range [0, 256],
    #  where 0 is black and 256 is white. A good value for fading our white
    #  text is in the range [100, 200].
    watermask = watermark.convert("L").point(lambda x: min(x, 100))
    # Apply this mask to the watermark image, using the alpha filter to 
    #  make it transparent
    watermark.putalpha(watermask)
    # Paste the watermark (with alpha layer) onto the original image and save it
    main.paste(watermark, None, watermark)
    main.save(".".join(main_image.split(".")[:-1]) + ".jpg", "JPEG")


# if __name__ == "__main__":
#     import os, glob
#     os.chdir("C:\Users\Kartheek\Desktop\Untitled Export")
#     imgs = glob.glob("*.jpg")
#     addWatermark(imgs[0], "MyLogoPNG.png")