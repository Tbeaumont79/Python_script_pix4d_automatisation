#-------------------------#
from createProject import *
from newpath import setNewPath
from openfile import openFile
from loadprojectwithtemplate import loadProject
import glob
import os
import zipfile
#-------------------------#

def     main():
    projectName = 'test.p4d'
    template = 'step123'
    projectImagePath = ''
    setUpNewProject(projectImagePath, projectName, template)
    openProjet(projectName)

if __name__ == '__main__':
    main()
