import os
import glob
# this function check is the fullprojectnamepath is already created
# return true if the project exist false if not

def     isProjectAlreadyCreated(projectNameFullPath):
    return os.path.isfile(projectNameFullPath)
