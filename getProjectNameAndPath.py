
def     projectNameWithoutExtension():
    projectName, _ = getProjectNameAndPath()
    projectNameWithoutExtension = projectName.split('.p4d')
    return projectNameWithoutExtension[0]

def     getProjectNameAndPath():
    projectName = 'FlightA.p4d'
    projectFullPath = '\\\\nt-nas\\CDRIN\Projets\\1718_67_CGM-auto\\source_acquisition\\FLIGHT 14 A\\DRONE\\'
    return projectName,projectFullPath
