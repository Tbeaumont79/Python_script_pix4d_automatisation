
def openProjet(projectName):
    setNewPath('C:\Program Files\Pix4Dmapper')
    os.system('./pix4dmapper.exe {0}'.format(projectName))
