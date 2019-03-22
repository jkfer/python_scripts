#!/usr/bin/python

# This is a script to list the contents of a directory, and its contents sizes:

import os
import sys
   

def list_item(dir):
    dir_size = os.stat(dir).st_size
    print('%s, %s \n' % (dir_size, dir))
    for roots, paths, files in os.walk(dir):
        if roots == dir:
            print('Contents of %s (bytes, path)' % dir)
            
            for file in files:
                abs_path_file = os.path.join(roots, file)
                size_file = os.stat(abs_path_file).st_size
                print('%s, %s' % (size_file, abs_path_file))
            
            for path in paths:
                abs_path = os.path.join(roots, path)
                size_path = os.stat(abs_path).st_size
                print('%s, %s' % (size_path, abs_path))
        



def run_main():
    try:
        os.listdir(sys.argv[1])
    except (OSError, IndexError) as e:
        print('Error.')
        print('Usage: dir_size.py <absolute_path_for_folder>')
        sys.exit(1)




if __name__ == '__main__':
    run_main()
    dir = sys.argv[1]
    list_item(dir)
    
