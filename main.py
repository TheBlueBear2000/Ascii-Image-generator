from PIL import Image
import numpy

CURRENTDIR = "projects/python/ascii_generator/"

imageName = input("Please give the name of the image:                           ")

asciiSize = int(input("Please input the width of the ascii (height will scale):     "))

gradient = ['NN','@@','##','WW','$$','99','88','77','66','55','44','33','22','11','00','??','!!','aa','bb','cc',';;','::','++','==','--',',,','..','__','  ']

image = Image.open(CURRENTDIR + imageName)

image = image.resize((asciiSize, int(image.height * (asciiSize/image.width))))

output = ""
pixels = numpy.array(image).tolist()


for y in range(int(image.height)):
    for x in range(int(image.width)):
        brightness = (max(pixels[y][x][0], pixels[y][x][1], pixels[y][x][2]) + min(pixels[y][x][0], pixels[y][x][1], pixels[y][x][2])) / 2
        gradientPoint = int(brightness/255 * len(gradient))
        if gradientPoint <= 0:
            gradientPoint = 1
        output += gradient[len(gradient) - gradientPoint]
        
    if y < int(image.height):
        output += "\n"
        
        
open(CURRENTDIR + imageName[:imageName.index(".",0)] + ".txt", "w").write(output)