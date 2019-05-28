#-------------------------#
import os
from newpath import setNewPath

def openProjet(projectNameFullPath):
    setNewPath('C:\\Program Files\\Pix4Dmapper')
    os.system('./pix4dmapper.exe {0}'.format(projectNameFullPath))
