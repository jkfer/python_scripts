#!/usr/bin/python

# Using the fabric module to collect the uptime days information only from several servers


import re
from fabric.api import run, env, hide


hosts = ['192.168.0.23', '192.168.0.24', '192.168.0.29', '192.168.0.30']
env.user = 'root'
env.key_filename = '/root/.ssh/id_rsa'


def getUptime():
    for host in hosts:
        env.host_string = host

        with hide('running', 'output'):
            time = run('uptime')
        
        time_re = re.compile(r'(up \d+ days)')

        res = time_re.search(time)
        print('%s is %s' % (host, res.group(0)))



if __name__ == "__main__":
    getUptime()
