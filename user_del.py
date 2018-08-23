#!/bin/python
import os
import shutil
import sys
import subprocess
import re


def del_user():
    user = sys.argv[1]

    # test if this is a valid user:
    with open('/etc/passwd', 'r') as f:
        file = f.read()

        if re.search(str(user), file):
            print('user is valid')


            # lock the user account
            subprocess.call(['passwd', '-l', user])


            # list all the files in the users home directory:
            home_dir = '/home/%s' % user
            backup_loc = '/backups/%s' % user
            if not os.path.exists(backup_loc):
                    # os.mkdir(backup_loc)
                    shutil.copytree(home_dir, backup_loc)
                    print('------BACKUP FILES DONE !!!-------')


            # kill all the processes being run by the user:
            print('Killing all processes run by %s' % user)
            subprocess.call(['killall', '-u', user])


        else:
            print('user is INVALID !!!!')


if __name__ == '__main__':
    del_user()
