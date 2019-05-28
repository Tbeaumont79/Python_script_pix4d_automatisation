import os
import glob
# this function check is the fullprojectnamepath is already created
# return true if the project exist false if not
def     getSize(startPath):
    totalSize = 0
    for dirpath, dirnames, filenames in os.walk(startPath):
        for f in filenames:
            filepath = os.path.join(dirpath, f)
            totalSize += os.path.getsize(filepath)
    return totalSize

def     isProjectAlreadyCreated(projectNameFullPath):
    return os.path.isfile(projectNameFullPath)

def     isProjectAlreadyBuild(projectNameFullPath, startPath):
    # first check the size of the directory
    # second (optional) check the number of element in the directory.
    numberOfElement = len(glob.glob(projectNameFullPath+'\*'))
    getSize = getSize(startPath);
    if (numberOfElement > 0 and getSize > 0):
        return False
    else:
        return True


