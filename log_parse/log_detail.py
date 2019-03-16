#!/usr/bin/python

# This is to parse the error_log file for httpd
# Using re.compile for this

import re
import os
import sys
import fnmatch


access_log_re = re.compile(r'(.*) - - \[(.*)\] (\".*\") ([0-9]{3}) (.*)')
error_log_re = re.compile(r'\[(.*)\] \[(.*)\] \[pid (\d+)\] \[client (.*)\] (.*)')


try:
    if os.path.isfile(sys.argv[1]):
        logfile = sys.argv[1]
        f = open(logfile, 'r')
    else:
        print('Input is not a valid file. Try again.')
        sys.exit(1)
except IndexError as err:
        print('No input file provided. Try again.')
        print('Usage: log_detail.py <access/error log>')
        sys.exit(1)
except NameError as err:
        print('Input file is not a valid file. Try again.')
        sys.exit(1)



def access_log_parse(line):
    if access_log_re.match(line):
        
        detail = access_log_re.match(line)
        time = detail.group(2)
        host = detail.group(1)
        status_code = detail.group(4)
        if detail.group(5) == '-':
            byte = '0'
        else:
            byte = detail.group(5)
            
        print('%s \t %s \t %s \t %s' % (time, host, status_code, byte))


def error_log_parse(line):
    if error_log_re.match(line):
        
        detail = error_log_re.match(line)
        time = detail.group(1)
        type = detail.group(2)
        pid = detail.group(3)
        client = detail.group(4)
        error = detail.group(5)
        
        print('%s \t %s \t %s \t %s \t %s' % (time, type, pid, client, error))


def log_parse():
    if fnmatch.fnmatch(logfile, '*access*'):
        for line in f.readlines():
            access_log_parse(line)
        f.close()
    elif fnmatch.fnmatch(logfile, '*error*'):
        for line in f.readlines():
            error_log_parse(line)
        f.close()


if __name__ == "__main__":
    log_parse()
