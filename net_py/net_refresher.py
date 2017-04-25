import string

def random_mac_gen():
	import random
	a = random.choice(string.hexdigits)
	b = random.choice(string.hexdigits)
	c = random.choice(range(10))

	new_mac = "%s4:6d:57:20:6d:%s%s" %(c,a,b)
	return new_mac
	

def mac_changer_ip_getter(mac):

	#change mac address
	import spoofmac
	spoofmac.set_interface_mac("wlan0",mac)

	#aquire ip address from the router
	import os
	os.system("dhclient wlan0")

	#get the gateway
	def gate():
		import netifaces
		d = netifaces.gateways()
		for v in d.itervalues():
			if type(v) == list:
				return v[0][0]

	#Send http request to get internet
	import requests
	n_mac = mac.upper()
	url = "http://%s/login?dst=&username=T-%s" %(gate(),n_mac)
	try:
		requests.get(url)
	except requests.exceptions.ConnectionError:
		print "Please wait ...\nReconnecting..."
		os.system('ifconfig wlan0 down')
		os.system('ifconfig wlan0 up')


mac_changer_ip_getter(random_mac_gen())
