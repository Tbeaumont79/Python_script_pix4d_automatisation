
from createProject import *
from openfile import openFile
from isProjectAlreadyCreated import *
from getProjectNameAndPath import getProjectNameAndPath

def     main():
    projectName,projectNameFullPath = getProjectNameAndPath()
    template = 'step123'
    projectImagePath = '\\\\nt-nas\\CDRIN\Projets\\1718_67_CGM-auto\\source_acquisition\\FLIGHT 14 A\\DRONE'
    if (isProjectAlreadyCreated(projectNameFullPath) == False):
        setUpNewProject(projectImagePath, projectName, template)
    else:
        print('Warning project is already build, you may change the name of the project')

if __name__ == '__main__':
    main()
