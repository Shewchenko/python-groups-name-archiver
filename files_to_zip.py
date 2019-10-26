import glob
import os
# importing required modules 
from zipfile import ZipFile 

#run
# C:\Users\Shew\python-3.7.4-embed-amd64\python.exe C:\Users\Shew\files_to_zip.py
# C:\Users\Shew\python-3.7.4-embed-amd64\python.exe .\files_to_zip.py

# path = 'C:\\Users\\Shew\\'
path = '.\\'
pathDir = path + 'arthives\\'


#files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]
# files = [f for f in glob.glob(path + 'test_ar\\' + "**/*.txt")]

# for f in files:
    # print(f)

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))
            # files.append(file)
for f in files:
    print(f)

file_name = path + "my_python_files.zip"
with ZipFile(file_name, 'w') as zip:
    for f in files:
        zip.write(path + f)
    print('Extracting all the files now...')
    zip.extractall() 
    print('Done!')