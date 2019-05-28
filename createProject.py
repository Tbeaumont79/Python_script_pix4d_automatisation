import glob
import os
from newpath import *
#-------------------------#
def     getAllImagePath(path):
    # get all the img from the dir
    image = glob.glob("*.jpg")
    imagePath = []
    i = 0
    countImage = len(image)
    # get the full path of all images
    while (i < countImage):
        getPathCommand = os.path.abspath(image[i])
        imagePath.append('<image path="'+getPathCommand+'"/>')
        i += 1
    return imagePath,countImage
#-------------------------#
# the function createProject build the project with all the xml that he need
def     createProject(template,imgPath,numberOfImage):
    version = '<software>'+'\n'+'<projectVersion>4.3.15</projectVersion>'+'\n\t'+'<p4dVersion>21</p4dVersion>'+'\n'+'<cameraModelVersion>19</cameraModelVersion>'+'\n'+'</software>'
    finalContent = '<?xml version="1.0" encoding="UTF-8"?>'+'\n'+'<pix4dmapper>'+'\n'+version+'\n'+'<options>'+'\n\t'+'<loadTemplate>'+template+'</loadTemplate>'+'\n'+'</options>'+'\n'+'<inputs>'+'\n'+'<images>'
    i = 0
    while i < numberOfImage:
        finalContent += '\n\t'+imgPath[i]
        i += 1

    finalContent += ''+'\n'+'</images>'+'\n'+'</inputs>'+'\n'+'</pix4dmapper>'
    return finalContent
#-------------------------#
def     setUpNewProject(projectImagePath, projectName, templateName):
    setNewPath(projectImagePath)
    imgFullPath,countImage = getAllImagePath(projectImagePath)
    createXml = createProject(templateName,imgFullPath,countImage)
    fd = openFile(projectName,'w')
    fd.write(createXml)
    fd.close()

#-------------------------#
