#!/usr/bin/python

import os
import subprocess
import sys
import re

# Grep each line found in a file on 'filename'


# get inputs from the user
filename = raw_input('Enter the filename to search for text in: ')
query_file = './files/lines.txt'


# check if file exists
if not os.path.isfile(filename):
    print('%s is not a valid filename. Exiting now.' % filename)
    sys.exit(1)



print('finding each line of %s in %s' % (query_file, filename))

def find_it(filename, query_file):
    for find_text in open(query_file, "r").readlines():
        for target_text in open(filename, "r").readlines():
            #print(find_text)
            #print(target_text)
            if re.findall(find_text.strip(), target_text.strip()):
                print('found %s: %s' % (find_text.strip(), target_text.strip()))


if __name__ == '__main__':
    find_it(filename, query_file)
