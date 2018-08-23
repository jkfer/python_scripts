#!/usr/bin/python

import subprocess
import os
import glob


# get all errors from the log files in /var/log using python (can use for cron practice) 

list = glob.glob('/var/log/*log')
for file in list:
    subprocess.call(['/bin/grep', '-iH', '--color', 'error', file.strip()])
    print('xxxxxxxxxxxxxxxxxxxxx--EOF--xxxxxxxxxxxxxxxxxxxxxxxxx')
