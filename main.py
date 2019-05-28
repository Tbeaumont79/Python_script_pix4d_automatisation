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
    projectName = 'FlightA.p4d'
    template = 'step123'
    projectImagePath = '\\nt-nas\\CDRIN\\Projets\\1718_67_CGM-auto\\source_acquisition\\FLIGHT 14 A\\DRONE​'
    setUpNewProject(projectImagePath, projectName, template)
    openProjet(projectName)

if __name__ == '__main__':
    main()
