#!/usr/bin/python

# This is a script to get all the running process that match the
# user input string (full or partial)
# Outputs to be user, process name, process ID, memory percentage
# Note: no matching process means - proccess part of the table will be empty

# To update - get matching dicts as output and if dict has valid values in it, then print table else 
# 'no process avail message'


import psutil
import sys
import re


usage = "get_process.py <process_name>"


if len(sys.argv) == 2:
    ps = sys.argv[1]
    ps_re = re.compile(r'%s' % ps)
else:
    print(usage)
    sys.exit(1)    



def get_process(ps):
    print('USER \t PROCESS \t PID \t MEM_PERCENT')
    p = psutil.process_iter()
    # proc = []
    for item in p:
        dict = item.as_dict(attrs=['username', 'name', 'pid', 'memory_percent'])
        user = dict['username']
        ps_name = dict['name']
        ps_pid = dict['pid']
        ps_mem = dict['memory_percent']
        if ps_re.search(ps_name):
            print('%s \t %s \t\t %s \t %s' % (user, ps_name, ps_pid, ps_mem))
            # proc.append(dict)
        else:
            continue
    # print proc



if __name__ == "__main__":
    get_process(ps)
