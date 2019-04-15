#!/usr/bin/python

# check for specific services listening on specified ports of various hosts in the network
# Assuming all the services are using the default ports. else the dict values will need to be modified
#
# Useful to check availability of services over the network and
# goal = Scale to email results and link script to cron schedule for monitoring.


# converting this to have email notifications incorporated.



import socket, smtplib
from texttable import Texttable
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


servers = [{'hostname': 'centos1.jkf.local', 'port': '80', 'service': 'http'},
	   {'hostname': 'mysql.jkf.local', 'port': '80', 'service': 'http'},
	   {'hostname': 'mysql.jkf.local', 'port': '3307', 'service': 'mysql'},
	   {'hostname': 'nagios.jkf.local', 'port': '80', 'service': 'http'},
	   {'hostname': 'www.google.com', 'port': '80', 'service': 'http'}]


# Find server status
def serv_status():
	status = []
	FAILED_SERVICE = []
	SUCCESS_SERVICE = []
	
	
	for server in servers:
		host = server['hostname']
		IP = socket.gethostbyname(host)
		port = server['port']
		service = server['service']

		# Checking if able to successfully connect to host
		
		try:
			c = socket.create_connection((host, port))
			status.append([host, IP, port, service, 'SUCCESS'])
			SUCCESS_SERVICE.append([host, IP, port, service, 'SUCCESS'])
		except:
			status.append([host, IP, port, service, 'FAILED'])
			FAILED_SERVICE.append([host, IP, port, service, 'FAILED'])
		finally:
			c.close()
	
	
	return status, FAILED_SERVICE, SUCCESS_SERVICE




# Wrap output in HTML (for failed services email. Table will be preserved)
def HTML_out(res):
	text = "<html><body><pre>%s</pre></body></html>" % res
	return text



# Create the table
def _texttable(status):
	T = Texttable()
	#T.set_cols_width([20, 20, 20, 20, 20])
	#T.set_cols_align(['c', 'c', 'c', 'c', 'c'])
	T.header(['Host', 'IP', 'Port', 'Service', 'Status'])
	for item in status:
		T.add_row(item)
	return T.draw()



# send email function (presently only for failed services)
def send_email(STATUS):
	smtp_server = 'smtp.gmail.com'
	port = 465

	sender = 'jkf.local@gmail.com'
	receiver = ['kvin0019@gmail.com']
	# enter email login passwod here:
	password = ''

	msg = MIMEMultipart('alternate')
	msg['To'] = ', '.join(receiver)
	msg['From'] = sender
	msg['Subject'] = 'CRITICAL: Service is down !'

	text = MIMEText(HTML_out(STATUS), 'html')
	msg.attach(text)

	c = smtplib.SMTP_SSL(smtp_server, port)
	c.set_debuglevel(1)
	c.login(sender, password)
	c.sendmail(sender, receiver, msg.as_string())
	c.quit()



# Call email function if any failed service
def dec_sendmail():
	
	status, FAILED_SERVICE, SUCCESS_SERVICE = serv_status()

	if len(FAILED_SERVICE) >= 1:
		send_status = _texttable(FAILED_SERVICE)
		send_email(send_status)
		#print('email sent!')
	else:
		print _texttable(status)




if __name__ == '__main__':
	dec_sendmail()


