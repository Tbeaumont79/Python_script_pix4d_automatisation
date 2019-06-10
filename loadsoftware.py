import os

def openProjet(projectName):
    os.startfile('\\\\nt-nas\\CDRIN\\Projets\\1718_67_CGM-auto\\source_acquisition\\FLIGHT 14 A\\DRONE\\'+projectName)

def     main():
    projectName = 'FlightA.p4d'
    openProjet(projectName)

if __name__ == '__main__':
    main()
