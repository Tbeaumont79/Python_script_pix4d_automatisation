#-------------------------#
from createProject import *
from openfile import openFile
from loadsoftware import *
#-------------------------#

def     main():
    projectName = 'FlightA.p4d'
    projectNameFullPath = '\\\\nt-nas\\CDRIN\Projets\\1718_67_CGM-auto\\source_acquisition\\FLIGHT 14 A\DRONE'+projectName
    template = 'step123'
    projectImagePath = '\\\\nt-nas\\CDRIN\Projets\\1718_67_CGM-auto\\source_acquisition\\FLIGHT 14 A\DRONE'
    setUpNewProject(projectImagePath, projectName, template)
    openProjet(projectNameFullPath)

if __name__ == '__main__':
    main()
