#!/usr/bin/python                                                                         
                                                                                          
# Using the fabric module to check the services available in the system.
# This is only for a practice purpose. Use a CM tool like Ansible for this.

# output can be modified to display in text table
# email function can be added to the script and linked to cron for moniroting and alerts


                                                                                          
import re
from fabric.api import run, env, hide                                                     
                                                                                          


hosts = [{'hostname': '192.168.0.23', 'services': ('httpd', 'mariadb')},
	 {'hostname': '192.168.0.24', 'services': ('httpd', 'mariadb')},
	 {'hostname': '192.168.0.29', 'services': ('httpd', 'mariadb')},
	 {'hostname': '192.168.0.30', 'services': ('httpd', 'mariadb')}]



env.user = 'joseph'                                                                         
env.key_filename = '/home/joseph/.ssh/id_rsa'                                                    


def get_services(host, service):

	status_re = re.compile(r'Active: .*(active|inactive)')
	
	env.host_string = host
	env.warn_only = True
	env.skip_bad_hosts = True
	env.disable_colors = True
	
	services = service
			

	with hide('warnings', 'running', 'output'):
		status = run('systemctl status %s' % service)
			

	for line in status.splitlines():
		if status_re.search(line):
			st = status_re.search(line)
			status = st.group(1)
		else:
			continue
					
	if status in ['active', 'inactive']:
		print('%s, %s, %s' % (host, service, status))
	else:
		print('%s, %s, unavailable' % (host, service))
					


		
def main():
	for item in hosts:
		for service in item['services']:
			#print('get_services %s, %s' % (item['hostname'], service))
			get_services(item['hostname'], service)



if __name__ == '__main__':
	main()

