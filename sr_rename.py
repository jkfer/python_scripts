#!/usr/bin/python

# This script is used to search and rename all the *.txt files 
# and move them to a seperate directory

import glob
import re
import os
import sys



folder_path = '/home/josephy/py_folder_1'
src_ext = 'txt'
new_ext = 'py'



def _rename(files, new_ext):
    files = glob.glob('%s/*%s' % (folder_path, src_ext))
    for file in files:
        new_filename = re.sub(src_ext, new_ext, file)
        print('renaming %s to %s ' % (file, new_filename))
        os.rename(file, new_filename)



if __name__ == "__main__":
    try:
        os.listdir(folder_path)
        _rename(files, new_ext)
    except OSError:
        print('%s is not a folder.' % (folder_path))
        sys.exit(1)

