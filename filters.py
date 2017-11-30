from PIL import Image
from PIL import ImageOps
from PIL import ImageFilter

filterlist = ["Choose a filter: ", "Deep Frier", "Grayscale", "Inverted", "Emoji"]

""" Deep fries images """
def deepfrier(image):
    # Applies various filters to the image
    image = image.filter(ImageFilter.DETAIL)
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    image = image.filter(ImageFilter.SHARPEN)
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
    inverted_image = ImageOps.invert(image) #inverts the color.
    inverted_image.save("meme.jpg")# Result picture.

""" Overlays emoji on picture. Takes an image, an emoji, coordinates at which to place the emoji,
    and an optional scale to shrink the emoji by """
    # Emoji list: emoji = ['100', 'B', 'Flame', 'Laughing', 'Okay']
def overlayEmoji(image, emoji, coordinates, shrinkscale=2):
    # makes path to emoji file and opens it
    emojidirect = 'Emoji/' + emoji.lower() + "-emoji.png"
    emojifile = Image.open(emojidirect)
    emojifile.thumbnail((int(emojifile.width/shrinkscale), int(emojifile.height/shrinkscale)), Image.ANTIALIAS)

    # finds center of emoji and computes new coordinates
    emojicenter = (int(emojifile.width/2), int(emojifile.height/2))
    coordinates = (coordinates[0] - emojicenter[0], coordinates[1] - emojicenter[1])

    # pastes emoji over image and saves as new image
    image.paste(emojifile, coordinates, emojifile)
    image.save("meme.jpg")
