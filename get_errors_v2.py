#!/usr/bin/python

import os
import fnmatch


# Using python to find errors in the files in provided the given path.

filename = '*boot*'
filepath = '/var/log/'
seperator = '======================================'

# print(filename)
# print(filepath)


# Function for finding string in selected set of files:
def find_errors(filename, filepath):

    #   Iterate through the files in the given path
    for path, dirs, files in os.walk(filepath):

        # For matching filenames (log files) - print/save filename
        for file_match in fnmatch.filter(files, filename):
            print(os.path.join(path, file_match))
            new_file = os.path.join(path, file_match)   
            print(seperator)
            
            # Look for 'error' or 'Error' in the new file: 
            for line in open(new_file).readlines():
                if ('error' or 'Error') in line:
                    print(line)


if __name__ == '__main__':
    find_errors(filename, filepath)
