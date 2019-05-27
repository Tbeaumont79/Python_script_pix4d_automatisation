from openfile import openFile

def loadProject(projectName):
    fd = openFile(projectName,'r')
    fd.read()
    print(fd)
    fd.close()
