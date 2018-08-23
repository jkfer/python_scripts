#!/usr/bin/python

import os
import subprocess
import sys

# Grep each line found in a file on 'filename'


# get inputs from the user
filename = raw_input('Enter the filename to search text in: ')
query_file = './files/lines.txt'


# check if file exists
if not os.path.isfile(filename):
    print('%s is not a valid filename. Exiting now.' % filename)
    sys.exit(1)


# define function to grep each line in a file
def grep_lines(filename, query_file):
    with open(query_file, "rb") as myfile:
        for line in myfile:
            subprocess.call(["/bin/grep", line.strip(), filename])


if __name__ == '__main__':
    grep_lines(filename, query_file)
