# Jaap Stefels -- NLRA2
# Code is created to export
from PIL import Image
from PIL import ImageFilter 
import os

# Converting all the different model outcomes (0,1,20,200,500 epochs) to only b&w
def black_and_white():
    for i in sorted(os.listdir("/Users/jaap/Desktop/leren_beslissen/accuracy")):
        if i.startswith("masked"):
            col = Image.open(i)
            gray = col.convert('L')
            bw = gray.point(lambda x: 255 if x >= lower and x <= upper  else 0, '1')
            bw.save("bw_{}".format(i))
        else:
            continue
# Calculating the accuracies for every file in map starting with bw

def calculating_accuracies():
    standard = "tile_0.jpg"

    # calculating different accuracies
    for i in sorted(os.listdir("/Users/jaap/Desktop/leren_beslissen/accuracy")):
        if i.startswith("bw"):
            mask = i
            standard = "tile_0.jpg"
            print(" ", mask)

            im            = Image.open(standard)
            imb           = Image.open(mask)
            pix_standard  = im.load()
            pix_mask = imb.load()
            width = 1024
            height = 1024
            whitestandard = 0
            whitemask = 0
            matchedwhite = 0
            match = 0
            for w in range(width):
                for h in range(height):
                    if pix_standard[(w,h)] == 255:
                        whitestandard += 1
                    if pix_mask[(w,h)] == 255:
                        whitemask += 1
                    if pix_mask[(w,h)] == 255 and pix_standard[(w,h)] == 255:
                        matchedwhite += 1
                        match += 1
                    if pix_mask[(w,h)] == 0 and pix_standard[(w,h)] == 0:
                        match += 1
                    # if pix_mask[(w,h)] == 0 and pix_standard[(w,h)] == 255:
                    #     match -= 1
                    # if pix_mask[(w,h)] == 255 and pix_standard[(w,h)] == 0:
                    #     match -= 1

#            print("     amount of white pixels in standard picture is:", whitestandard)
#            print("     amount of white pixels in mask picture is:", whitemask)
#            print("     amount of matchedwhite pixels minus differences is:", count)
#            print("     amount of matchedwhite pixels is:", matchedwhite)
            overlay = (matchedwhite/whitestandard)*100
            print("     Overlay is:", overlay)
            pixels = height * width
            accuracy = (match/pixels) * 100
            print("     Accuracy", accuracy)
            print("\n")
            print("     Amount of white pixels in standard picture is: ", whitestandard)
            print("     Percentage white pixels over total pixels in standard picture is: ", (whitestandard / pixels) * 100)


lower = 0
upper = 0
# The four black and white situations to measure accuracy with
for sit in range(4):
    print("\n")
    # Mark all the non-black colors as white, the rest black
    if sit == 0:
        lower = 1
        upper = 255
        print("Situation 0: Mark all the non-black colors as white, the rest black.")
    # Mark colors from RGB 80-255 as white, the rest black
    if sit == 1:
        lower = 80
        upper = 255
        print("Mark colors from RGB 80-255 as white, the rest black.")
    # Mark colors from RGB 160-255 as white, the rest black
    if sit == 2:
        lower = 160
        upper = 255
        print("Mark colors from RGB 160-255 as white, the rest black.")
    # Mark only RGB 255(white) as white, the rest black
    if sit == 3:
        lower = 255
        upper = 255
        print("Mark only RGB 255(white) as white, the rest black.")
    # print(lower)
    # print(upper)

    # Execute converting with the appropiate color conversion
    black_and_white()
    # Calculate the accuracy for the current color scheme
    calculating_accuracies()
    sit += 1
    
