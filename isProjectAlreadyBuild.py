import os
import glob
from getProjectNameAndPath import *
# this function check is the fullprojectnamepath is already created
# return true if the project exist false if not
def     getSize(startPath):
    totalSize = 0
    for dirpath, dirnames, filenames in os.walk(startPath):
        for f in filenames:
            filepath = os.path.join(dirpath, f)
            totalSize += os.path.getsize(filepath)
    return totalSize

def     isProjectAlreadyBuild(projectName, startPath):
    # first check the size of the directory
    # second (optional) check the number of element in the directory.
    numberOfElement = len(glob.glob(startPath+'\*'))
    size = getSize(startPath)
    if (numberOfElement > 0 and size > 0):
        msg = "the project is already build"
    else:
        msg = "the project is not build"
    print(msg)

def main():
    projectName, projectNameFullPath = getProjectNameAndPath()
    projectNameFullPath = projectNameFullPath+'\\'+projectName
    isProjectAlreadyBuild(projectName,projectNameFullPath)

if __name__ == '__main__':
    main()
