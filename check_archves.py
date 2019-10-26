import os
from os.path import isfile, join, splitext
import zipfile
from contextlib import closing

# C:\Users\Shew\python-3.7.4-embed-amd64\python.exe .\check_archves.py

path = '.\\'

archives = [f for f in os.listdir(path) if f.endswith('.zip')]
print(archives)
f= open( path + "check_output_list", "w+")
for nameArchive in archives:
    with closing(zipfile.ZipFile(path + nameArchive)) as archive:
        count = len(archive.infolist())
        msg = "\n name: " +  nameArchive  + " --> count files: " + str(count) + "\n"
        print(msg)
        f.write(msg)
f.close()