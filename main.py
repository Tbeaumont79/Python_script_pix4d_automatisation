from createProject import *

def     main():
    setNewPath('C:\\Users\\beaumontt\\Desktop\\reconstruction2\\FLIGHT 14 A\\DRONE')
    imgFullPath,countImage = getAllImagePath('C:\\Users\\beaumontt\\Desktop\\reconstruction2\\FLIGHT 14 A\\DRONE')
    createXml = createProject('step123',imgFullPath,countImage)
    fd = openFile('test.p4d','w')
    fd.write(createXml)
    fd.close()

if __name__ == '__main__':
    main()
    