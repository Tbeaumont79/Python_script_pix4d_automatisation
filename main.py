
from createProject import *
from openfile import openFile
from loadsoftware import *
from isProjectAlreadyCreated import *
from zipdir import zipProject
from cpyfolder import copyDirectory

#-------------------------#

def     main():
    projectName = 'FlightA.p4d'
    projectNameFullPath = '\\\\nt-nas\\CDRIN\Projets\\1718_67_CGM-auto\\source_acquisition\\FLIGHT 14 A\\DRONE\\'+projectName
    template = 'step123'
    projectImagePath = '\\\\nt-nas\\CDRIN\Projets\\1718_67_CGM-auto\\source_acquisition\\FLIGHT 14 A\\DRONE'
    if (isProjectAlreadyCreated(projectNameFullPath) == False):
        setUpNewProject(projectImagePath, projectName, template)
    else:
        print('Warning project is already build, you may change the name of the project')
    projectNameWithoutExtension = projectName.split('.');
    zipProject(projectNameWithoutExtension[0]);

    #openProjet(projectNameFullPath)

if __name__ == '__main__':
    main()
