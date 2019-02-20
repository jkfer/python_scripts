#!/usr/bin/python

# print all available repo links with enabled/disabled status (this only looks for available and active baseurls)
# re.match only matches from the beginning of the string

import sys
import os
import re
import linecache


for root, path, files in os.walk('/etc/yum.repos.d/'):
    
    for file in files:
        new_file = os.path.join(root, file)
        # print(new_file)
        
        f=open(new_file, 'r')
        
        line_num = 0
        
        for line in f.readlines():
            line_num += 1
            if re.match('baseurl=http', line.strip()):
                BaseURL = line.strip()
                
                # search for available repo status in the following 5 lines:

                for i in range(line_num+1, line_num+6):
                    if re.match('enabled', linecache.getline(new_file, i)):
                        Status = linecache.getline(new_file, i).strip()
            
                print("%s \t %s" % (Status, BaseURL))
