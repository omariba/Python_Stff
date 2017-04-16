import requests
import spoofmac
import random
import string
import os

def random_mac_gen():
	a = random.choice(string.hexdigits)
	b = random.choice(string.hexdigits)
	c = random.choice(range(10))

	new_mac = "%s4:6d:57:20:6d:%s%s" %(c,a,b)
	return new_mac
	

def mac_changer_ip_getter(mac):
	spoofmac.set_interface_mac("wlan0",mac)

	os.system("dhclient wlan0")

	http://172.16.50.1/login?dst=&username=T-34%3A6D%3A57%3A20%3A6D%3A1E
	url = "http://172.16.50.1/login?dst=&username=T-%s" %(mac)
	requests.get(url)

	os.system("ping -c 5 8.8.8.8")


mac_changer_ip_getter(random_mac_gen())
