# importing required modules 
from zipfile import ZipFile 
  
def extractMyFile():
  # specifying the zip file name 
  file_name = "test.zip"
    
  # opening the zip file in READ mode 
  with ZipFile(file_name, 'r') as zip: 
      # printing all the contents of the zip file 
      zip.printdir() 
    
      # extracting all the files 
      zip.extractall() 
      print('Done!') 


def zipMyFile():
    file_name = 'test.zip'

    # opening the 'Zip' in writing mode
    with ZipFile(file_name, 'a') as file:
        # append mode adds files to the 'Zip'
        # you have to create the files which you have to add to the 'Zip'
        file.write('test.txt')
        print('Files added to the Zip')

    with ZipFile(file_name, 'r') as file:
        print(file.namelist())


zipMyFile()
extractMyFile()