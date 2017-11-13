from easygui import *
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter
import PIL.ImageOps
import os

"""

"""
def invertColor():    
    image= Image.open("meme.jpg") # Opens up picture.
    inverted_image = PIL.ImageOps.invert(image) #inverts the color.
    inverted_image.save("meme.jpg")# Result picture.
   
def blackAndWhite():
    image_file = Image.open("meme.jpg") #Opens up picture.
    image_file=image_file.convert('1')  #Converts image black to white.
    image_file.save('meme.jpg') # Result picture.
"""
This function overlays text on the meme image in white or black.

"""
def text():
    msg = "Enter Meme Captions"
    title = "MemeGenerator"
    wb = buttonbox("Would You Like White or Black Text?", title, ("White", "Black"))

    #determines text color
    if (wb == "White"):
        color = 255
    if (wb == "Black"):
        color = 0
                      
    fieldNames = ["Top Caption", "Bottom Caption"]
    fieldValues = []
    fieldValues = multenterbox(msg, title, fieldNames)
    #Makes the text Upper Case
    fieldValues[0] = fieldValues[0].upper()
    fieldValues[1] = fieldValues[1].upper()
    
    # Centers text
    meme = Image.open("copy.jpg")
    imageSize = meme.size
    fontSize = int(imageSize[1]/5)
    font = ImageFont.truetype("impact.ttf", fontSize)
    topTextSize = font.getsize(fieldValues[0])
    bottomTextSize = font.getsize(fieldValues[1])
    # Resizes text, if size of text is bigger than image
    while topTextSize[0] > imageSize[0] - 20 or bottomTextSize[0] > imageSize[0] - 20:
        fontSize = fontSize - 1
        font = ImageFont.truetype("impact.ttf", fontSize)
        topTextSize = font.getsize(fieldValues[0])
        bottomTextSize = font.getsize(fieldValues[1])

    topTextPosX = (imageSize[0]/2) - (topTextSize[0]/2)
    bottomTextPosX = (imageSize[0]/2) - (bottomTextSize[0]/2)
    bottomTextPosY = (imageSize[1] - bottomTextSize[1]- 10)

    drawTop = ImageDraw.Draw(meme)
    drawBottom = ImageDraw.Draw(meme)
    drawTop.text((topTextPosX,0), fieldValues[0],(color,color,color), font=font) #(location, string, color, font)
    drawBottom.text((bottomTextPosX, bottomTextPosY), fieldValues[1],(color,color,color), font=font)
    meme.save("meme.jpg")
"""
This function is called when the user wants to add some sort of image filter.
It then calls that image manipulation function.
"""
def colorManipulation():
    title = "Meme Generator"
    choice = buttonbox('What manipulation would you like?', title, ('Invert Color', 'Black and White'))
    if (choice == 'Invert Color'):
        invertColor()
    elif (choice == 'Black and White'):
        blackAndWhite()
    # elif (choice == 'Rotate 90 Left'):
    #     rotate90Left()
    # elif (choice == 'Rotate 90 Reft'):
    #     rotate90Right()
    # elif (choice == 'Flip Upsidedown'):
    #     rotate180()

"""
Asks user to confirm they like the meme they created.
Gives option to redo text or apply filters.
If yes meme is saved as user provided file name.
"""            
def confirmation():
    while True:
        meme = Image.open("meme.jpg")
        msgConfirm = "Do you like this picture?"
        ynChoices = ["Yes", "Redo Text", "Manipulate Colors", "No"]
        reply = buttonbox(msgConfirm, image="meme.jpg", choices=ynChoices)
        if reply == ("Yes"):
            saveName = enterbox("What do you want to save the meme as?", "Meme Generator", "Save Name")
            meme.save(saveName + ".jpg")
            break
        elif reply == ("Redo Text"):
            text()
        elif reply == ("Manipulate Colors"):
            colorManipulation()
        else:
            break
        
    
"""
Main function where you choose the meme then redirects to text manipulation options.
Calls text() and confirmation()
"""   
def main():
    #Creates the Relative File Path
    folder = os.path.dirname(os.path.realpath('__file__'))
    fileName = os.path.join(folder, '../MemeGenerator/Memes/')
    fileName = os.path.abspath(os.path.realpath(fileName))
    title = 'Meme Generator'
    choices =['Awkward Moment Seal', 'Bad Luck Brian', 'Brace Yourself', 'Condescending Wonka', 'Desk Flip', 'Futurama Fry', 'Philosoraptor', 'Scumbag Steve', 'Success Kid', 'Create Your Own Meme']
    #User selects the meme of choice
    memeSelection = choicebox ('Select Meme', title, choices)
    if(memeSelection == "Create Your Own Meme"): #Allows user to select their own picture to meme
        memePath = fileopenbox()
    else:
        memePath =  fileName + "\\" + memeSelection + ".jpg"


    meme = Image.open(memePath)
    #meme.show() #Shows the desired image
    meme.save("copy.jpg") #Saves for further use
    meme = Image.open("copy.jpg") #Allows the new meme to be used

    text()
    confirmation()

while True:
    main()
    loop = buttonbox("Would you like to create a meme?", "Meme Generator", ["Yes", "No"])
    if ( loop == 'No' ):
        break
    

    
   
