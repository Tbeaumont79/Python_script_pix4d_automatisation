import shutil
from newpath import *

def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

def main():
    setNewPath('\\\\nt-nas\\CDRIN\Projets\\1718_67_CGM-auto\\source_acquisition\\FLIGHT 14 A\\DRONE');
    srcFullPath = './FlightA.zip'
    destFullPath = '\\\nt-nas\\CDRIN\\Projets\\1718_67_CGM-auto\\archives'

if __name__ == '__main__':
    main()
