import os
from os.path import isfile, join, splitext
import zipfile
from contextlib import closing

path = '.\\'

archives = [f for f in os.listdir(path) if f.endswith('.zip')]
print(archives)
f= open( path + "check_output_list", "w+")
for nameArchive in archives:
    with closing(zipfile.ZipFile(path + nameArchive)) as archive:
        count = len(archive.infolist())
        print(count)
        f.write("name: " +  nameArchive  + " --> count files: " + str(count) + "\n")
f.close()