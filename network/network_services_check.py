#!/usr/bin/python

# check for specific services listening on specified ports of various hosts in the network
# Assuming all the services are using the default ports. else the dict values will need to be modified
#
# Useful to check availability of services over the network and
# goal = Scale to email results and link script to cron schedule


import socket
from prettytable import PrettyTable



servers = [{'hostname': 'centos1.jkf.local', 'port': '80', 'service': 'http'},
	   {'hostname': 'mysql.jkf.local', 'port': '80', 'service': 'http'},
	   {'hostname': 'mysql.jkf.local', 'port': '3306', 'service': 'mysql'},
	   {'hostname': 'nagios.jkf.local', 'port': '80', 'service': 'http'},
	   {'hostname': 'www.google.com', 'port': '80', 'service': 'http'}]




def serv_status():
	
	status = []
	
	for server in servers:
		host = server['hostname']
		IP = socket.gethostbyname(host)
		port = server['port']
		service = server['service']

		# Checking if able to successfully connect to host
		
		try:
			c = socket.create_connection((host, port))
			status.append([host, IP, port, service, 'SUCCESS'])
		except:
			status.append([host, IP, port, service, 'FAILED'])
		finally:
			c.close()
	
	return status




def _table():
	row_item = serv_status()
	T = PrettyTable(['Host', 'IP', 'Port', 'Service', 'Status'])
	for item in row_item:
		T.add_row(item)
	print(T)
	




if __name__ == '__main__':
	serv_status()
	_table()


