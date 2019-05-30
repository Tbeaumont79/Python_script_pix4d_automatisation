# import required modules
import os
import zipfile

# Declare the function to return all file paths of the particular directory
def retrieve_file_paths(dirName):
  filePaths = []
  # Read all directory, subdirectories and file lists
  for root, directories, files in os.walk(dirName):
    for filename in files:
        # Create the full filepath by using os module.
        filePath = os.path.join(root, filename)
        filePaths.append(filePath)

  return filePaths


def zipProject(dirname):
  dir_name = dirname
  # Call the function to retrieve all files and folders of the assigned directory
  filePaths = retrieve_file_paths(dir_name)
  # printing the list of all files to be zipped
  print('The following list of files will be zipped:')
  for fileName in filePaths:
    print(fileName)
  # writing files to a zipfile
  zip_file = zipfile.ZipFile(dir_name+'.zip', 'w')
  with zip_file:
    # writing each file one by one
    for file in filePaths:
      zip_file.write(file)

  print(dir_name+'.zip file is created successfully!')

def main():
    projectNameWithoutExtension = 'FlightA';
    zipProject(projectNameWithoutExtension);

  if __name__ == '__main__':
      main()
