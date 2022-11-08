#takes in a file name, side length(size), and location of file (path)
#returns the image cropped into a square and then scaled to the requested size for each side length
def cropSquare(filename,size,path):
    #stores the path to the specific image in variable fullpath
    fullpath = path + '\\' + filename
    im = Image.open(fullpath)
    #Generates a scale based off of whether the height or length is longer
    if (im.width < im.height):
        scale = size/im.width
    else:
        scale = size/im.height
    
    resizeImage = Image.new("RGB", (int(scale*im.width), int(scale*im.height)))
    for i in range(0, resizeImage.width):
        for j in range(0, resizeImage.height):
            RGB = im.getpixel((int(i/scale), int(j/scale)))
            resizeImage.putpixel((i, j), (RGB[0], RGB[1], RGB[2]))

    os.remove(path + "//" + filename)
    resizeImage.save(path + "//" + filename, 'PNG')
    return resizeImage
