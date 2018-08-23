#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()
# print(args.filename)

try:
    f = open(args.filename)
except IOError as err:
    print("Error: file is not found")
else:
    with f:
        limit = args.limit
        lines = f.readlines()
        lines.reverse()

    if limit:
        lines = lines[:limit]

    for line in lines:
        # the [::-1] reverses the line
        print(line.strip())[::-1]

finally:
    print("\n We're FINISHED ....... !!!!! \n")

