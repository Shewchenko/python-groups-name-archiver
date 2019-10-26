import glob
import os
from os.path import isfile, join, splitext
import zipfile

#run
# C:\Users\Shew\python-3.7.4-embed-amd64\python.exe C:\Users\Shew\files_to_zip.py
# C:\Users\Shew\python-3.7.4-embed-amd64\python.exe .\files_to_zip.py

path = '.\\'
pathArcive = path + 'arthives\\'


filesDir = [f for f in os.listdir(path) if isfile(join(path, f))] 
for file in filesDir:
    if '.py' in file or '.gitignore' in file:
        filesDir.remove(file)

for file in filesDir:
    if '.zip' in file:
        filesDir.remove(file)
# print(filesDir) 

for file in filesDir:
    name, exten = splitext(file)
    nameArchive = path + name + ".zip"

    targ = 'w'
    if isfile(nameArchive):
        targ = 'a'
        
    zip = zipfile.ZipFile(nameArchive,targ)
    zip.write(path + file)
    zip.close()