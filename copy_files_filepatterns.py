#!/usr/bin/python

# ***Automating for required large scale file operations for client 
# This script is for finding a list of files / filename patterns in a designated folder location 
# and copy them over to a particular given folder.
 
# Copying over the files to a seperate directory.



import os
import subprocess
import sys
import fnmatch
import shutil



# Input the absolute path of the file with file patterns:
filename = raw_input('Enter the absolute path of the file containing filenames:')


# Find filename patterns here:
query_location = '/home/'


# Copy files over to this location:
copy_filesover = '/home/cloud_user/BACKUP/'


# Check if user input file and locations are valid 
def check_inputs(filename, query_location):
    if not os.path.isfile(filename) or not os.path.isdir(query_location) or not os.path.isdir(copy_filesover):
        print('invalid file %s or location %s' % (filename, query_location))
        sys.exit(1)
    else:
        print('Input check: PASSED.')


# Function definition for copying files over to the backup location

def copy_files(query_location, filename):
#   prepare the input file for parsing through line by line: 
    with open(filename) as f:
        pattern_list = f.readlines()

#   for each line in the pattern file
    for file_pattern in pattern_list:
        for root, dirs, files in os.walk(query_location):
#           for the each available pattern matches of files set: 
            for filematch in fnmatch.filter(files, file_pattern.strip()):
                if 'BACKUP' not in root:
#                   print(filematch)
#                   print(root)
                    print('copying %s over to %s%s' % (os.path.join(root, filematch), copy_filesover, filematch))
                    shutil.copy(os.path.join(root, filematch), copy_filesover)


check_inputs(filename, query_location)
copy_files(query_location, filename)            
