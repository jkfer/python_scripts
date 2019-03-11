#!/usr/bin/python

# File for replacing document root of a specific virtual host
# using re.search(), re.sub()
# printing the output to stdout


import os
import re
import fnmatch



match_str = '*.conf'
conf_files = []
new_DocRoot = "/var/www/html/newdoc/root"
virthost_regexp = r'^<(VirtualHost) ([a-zA-Z]+):([0-9]+)>$'
docroot_regexp = r'(DocumentRoot) (.*)$'
location = '/etc/httpd'


# Making a list containing the *.conf files
for root, path, files in os.walk(location):
    for match in fnmatch.filter(files, match_str):
        # Getting the output as a list:
        conf_files.append(os.path.join(root, match))


def docRoot_replace():
# find each file and the line number which has <VirtualHost.*
    for files in conf_files:
        if re.findall(r'</VirtualHost>', open(files).read()):
            print('==========================================')
            print(files)
            print('==========================================')

            with open(files) as f:
                       
                # Iterate through the lines of the file
                for line in f:

                    # if the line starts with '<VirtualHost vhost1'
                    if re.search(virthost_regexp, line):
                        print(line.rstrip())
                        match = re.search(virthost_regexp, line)
                        
                        if match.group(2) == 'local':
                            for line in f:
                                if re.search(docroot_regexp, line):
                                    doc_root = re.search(docroot_regexp, line)
                                    new_line = re.sub(doc_root.group(2), new_DocRoot, line)
                                    line = new_line
                                print(line.rstrip())
                    
                        print(line.rstrip())    




if __name__ == '__main__':
    docRoot_replace()



