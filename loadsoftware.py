import os
from getProjectNameAndPath import getProjectNameAndPath

def openProjet(projectName):
    os.startfile('\\\\nt-nas\\CDRIN\\Projets\\1718_67_CGM-auto\\source_acquisition\\FLIGHT 14 A\\DRONE\\'+projectName)

def     main():
    projectName,_ = getProjectNameAndPath()
    openProjet(projectName)

if __name__ == '__main__':
    main()
