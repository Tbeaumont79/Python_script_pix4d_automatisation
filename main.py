from createProject import *
from newpath import setNewPath
from openfile import openFile
from loadprojectwithtemplate import loadProject

def     main():
    setNewPath('C:\\Users\\beaumontt\\Desktop\\reconstruction2\\FLIGHT 14 A\\DRONE')
    imgFullPath,countImage = getAllImagePath('C:\\Users\\beaumontt\\Desktop\\reconstruction2\\FLIGHT 14 A\\DRONE')
    createXml = createProject('step123',imgFullPath,countImage)
    fd = openFile('test.p4d','w')
    fd.write(createXml)
    fd.close()

if __name__ == '__main__':
    main()
