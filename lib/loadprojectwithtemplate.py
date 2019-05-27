from openfile import openFile

def loadProject(projectName):
    fd = openFile(projectName,'r')
    fd = fd.split()
    print(fd)
