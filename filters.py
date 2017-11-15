from PIL import Image
from PIL import ImageFilter

""" Deep fries an image. Takes an optional second parameter.
    Second parameter is a boolean specifiying how distorted the image is."""
def deepfrier(image, doublefry=False):
    # Applies various filters to the image
    image = image.filter(ImageFilter.DETAIL)
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    image = image.filter(ImageFilter.SHARPEN)

    # Adds an extra level of crispiness
    if doublefry is True:
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)

    image.save("meme.jpg")

""" Converts to grayscale """
def grayscale(image):
    new_list = []
    newimage = Image.new("RGB", (image.width, image.height), "white")
    for p in image.getdata():
        intensity = int((p[0] + p[1] + p[2])/3)
        temp = (intensity, intensity, intensity)
        new_list.append(temp)
    newimage.putdata(new_list)
    newimage.save("meme.jpg")

def invertColor(image):
    inverted_image = PIL.ImageOps.invert(image) #inverts the color.
    inverted_image.save("meme.jpg")# Result picture.
