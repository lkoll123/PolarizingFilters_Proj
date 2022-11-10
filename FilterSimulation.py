# Import and initialize pygame library
import pygame
pygame.init()
from PIL import Image
import os

# Set up drawing window
screen = pygame.display.set_mode([200,200])
pygame.display.set_caption('FilterSim')
clock = pygame.time.Clock()

testFile = 'pumpkin.jpg'
testPath = 'C:/Users/cwo06/Desktop/Algorithm Design/Images'

#create test arrs that indicate the color the pixels start at and what color they should turn to
#Representative of circle filter colors
pixInput = [[0 for i in range(20)] for j in range(20)]

pixAlter = [[0 for i in range(20)] for j in range(20)]

pixOutputTest = [[0,0,0,0,0,0,0,0,0,0],
            [0,200,0,0,200,0,200,200,200,10],
            [0,200,0,0,200,0,0,200,10,40],
            [0,200,200,200,200,0,0,200,40,70],
            [0,200,0,0,200,0,10,200,70,100],
            [0,200,0,0,200,10,200,200,200,130],
            [0,0,0,0,10,40,70,100,130,160],
            [0,0,0,10,40,70,100,130,160,190],
            [0,0,10,40,70,100,130,160,190,220],
            [0,10,40,70,100,130,160,190,220,250]]



def grayScale(filename, path):
    fullpath = path + '/' + filename
    im = Image.open(fullpath)
    Width, Height = im.size
    scale = 2.83 #roughly 255/90

    newImg = Image.new("RGB", (Width, Height))
    for x in range (0, Width):
        for y in range (0, Height):
            originalrgb = im.getpixel((x, y))
            newrgb = int(0.299 * originalrgb[0] + 0.587 * originalrgb[1] + 0.114 * originalrgb[2])
            Scalergb = int(newrgb - (newrgb%scale))
            newImg.putpixel((x, y), (newrgb, newrgb, newrgb))
    os.remove(path + "/" + filename)
    newImg.save(path + "/" + filename, 'PNG')
    newImg.show



def cropSquare(filename,size,path):
    #stores the path to the specific image in variable fullpath
    fullpath = path + '/' + filename
    im = Image.open(fullpath)
    #Generates a scale based off of whether the height or length is longer
    if (im.width < im.height):
        scale = size/im.width
        resizeImage = Image.new("RGB", (int(scale*im.width), int(scale*im.width)))
    else:
        scale = size/im.height
        resizeImage = Image.new("RGB", (int(scale*im.height), int(scale*im.height)))
    for i in range(0, resizeImage.width):
        for j in range(0, resizeImage.height):
            RGB = im.getpixel((int(i/scale), int(j/scale)))
            resizeImage.putpixel((i, j), (RGB[0], RGB[1], RGB[2]))

    os.remove(path + "/" + filename)
    resizeImage.save(path + "/" + filename, 'PNG')
    return resizeImage

def imToArr(image):
    colorArr = [[0 for i in range(image.width)] for j in range(image.width)]
    for i in range(0, image.width):
        for j in range(0, image.height):
            RGB = image.getpixel((i,j))
            colorArr[i][j] = RGB[0]
    return colorArr


cropSquare(testFile, 20, testPath)
grayScale(testFile, testPath)

pixOutput = imToArr(cropSquare(testFile, 20, testPath))

print(imToArr(cropSquare(testFile, 20, testPath)))


def game_loop():
    exit = False
    time = 0
    stop = True
    while not exit:
        clock.tick(60)
        if not stop and time <= 100000:
            time += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())
            elif event.type == pygame.KEYUP:
                if pygame.key.key_code("space") == pygame.K_SPACE:
                    stop = not stop
                    print("time:", time)
        screen.fill((0,0,0))

######### draw stuff ##########
        #setup variables to be used later
        if time == 0:
            i = 0
            j = 0
            totalDif = 0

        if i < 20:
            #find the total amount the color needs to change for first circle(index)
            startDif = pixOutput[i][j] - pixInput[i][j]
            #find how much further the color needs to change
            runDif = pixOutput[i][j] - pixAlter[i][j]

            #if the color still needs to change, either add or subtract until it is equal to the wanted color
            if runDif > 0:
                pixAlter[i][j]=pixInput[i][j] + time-totalDif
            elif runDif < 0:
                pixAlter[i][j]=pixInput[i][j] - (time-totalDif)

            #if the color is right, move to the next circle (index in the array)
            elif j < 20:
                if startDif > 0:
                    totalDif+=startDif
                elif startDif < 0:
                    totalDif-=startDif
                j+=1

            #if all colors have been changed in row, move to the next row
            if j == 20:
                j=0
                i+=1

        #draw the circles on the screen
        for x in range(20):
            for y in range(20):
                color = pixAlter[y][x]
                pygame.draw.circle(screen,(color,color,color),(5+x*10,5+y*10),5)


        pygame.display.update()

game_loop()
pygame.quit()
quit()
