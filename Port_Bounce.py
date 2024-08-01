import pandas as pd
from netmiko import Netmiko
from netmiko import ConnectHandler
from pandas import DataFrame
from datetime import datetime
import concurrent.futures
import easygui
import time

# CLI PARAMETERS:
USERNAME = ''
PASS = ''
ENABLE = ''

def bounce_ports(switchip):
	try:
		login = {
   		"host": switchip,
   		"username": USERNAME,
   		"password": PASS,
   		"device_type": "cisco_ios",
   		"secret": ENABLE}
		net_connect = Netmiko(**login)
		net_connect.enable()
		for port in portlist[switchip]:
			print(f'Bouncing {port} on {switchip}')
			net_connect.send_config_set([f'int {port}', 'shut'])
			time.sleep(5)
			net_connect.send_config_set([f'int {port}', 'no shut'])
		net_connect.disconnect()
	except:
		print(f'{switchip} had a problem. Port was: {port}')

def main():
	portDF = pd.read_excel(easygui.fileopenbox())

	for ip,port in zip(portDF['NAS-IP-Address'],portDF['NAS-Port-Id']):
		if ip not in portlist:
			portlist[ip] = [port]
		else:
			portlist[ip].append(port)

	with concurrent.futures.ThreadPoolExecutor(max_workers=75) as executor:
		executor.map(bounce_ports,portlist.keys())

	print(datetime.now()-startTime)

if __name__ == '__main__':
	# Creating empty dict to hold data to process
	startTime = datetime.now()
	portlist = {}
	main()
