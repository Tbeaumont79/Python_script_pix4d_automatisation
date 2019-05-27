import glob
import os

def     getAllImagePath(path):
    image = glob.glob("*.jpg")
    imagePath = []
    i = 0
    countImage = len(image)
    while (i < countImage):
        getPathCommand = os.path.abspath(image[i])
        imagePath.append('<image path="'+getPathCommand+'"/>')
        i += 1
    return imagePath,countImage

def     createProject(template,imgPath,numberOfImage):
    version = '<software>'+'\n'+'<projectVersion>4.3.15</projectVersion>'+'\n\t'+'<p4dVersion>21</p4dVersion>'+'\n'+'<cameraModelVersion>19</cameraModelVersion>'+'\n'+'</software>'
    finalContent = '<?xml version="1.0" encoding="UTF-8"?>'+'\n'+'<pix4dmapper>'+'\n'+version+'\n'+'<options>'+'\n\t'+'<loadTemplate>'+template+'</loadTemplate>'+'\n'+'</options>'+'\n'+'<inputs>'+'\n'+'<images>'
    i = 0
    while i < numberOfImage:
        finalContent += '\n\t'+imgPath[i]
        i += 1

    finalContent += ''+'\n'+'</images>'+'\n'+'</inputs>'+'\n'+'</pix4dmapper>'
    return finalContent
