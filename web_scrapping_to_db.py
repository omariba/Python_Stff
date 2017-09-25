from bs4 import BeautifulSoup
import requests

u_url = raw_input("enter url(without http://): ")
fin_url = "http://"+u_url

r_data = requests.get(fin_url)
html = r_data.text
soup = BeautifulSoup(html,'html.parser')

pics = soup.findAll('div',{'class':'sku -gallery'})

for prod in pics:
	each_lap = prod.findAll('h2',{'class':'title'})
	for lap_name in each_lap:
		name = lap_name.findAll('span',{'class':'name'})
		for i in name:
			print i.text
