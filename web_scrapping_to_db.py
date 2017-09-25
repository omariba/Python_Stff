from bs4 import BeautifulSoup
import requests
import MySQLdb as mysql

conn = mysql.connect('localhost','root',"",'test_nelly')
edit = conn.cursor()

u_url = raw_input("enter url(without http://): ")
fin_url = "http://"+u_url

r_data = requests.get(fin_url)
html = r_data.text
soup = BeautifulSoup(html,'html.parser')

pics = soup.findAll('div',{'class':'sku -gallery'})

for prod in pics:
	each_lap = prod.findAll('h2',{'class':'title'})
	each_lap_price = prod.findAll('div',{'class':'price-container clearfix'})
	for lap_name,lap_price in zip(each_lap,each_lap_price):
		name = lap_name.findAll('span',{'class':'name'})
		price_P = lap_price.findAll('span',{'class':'price-box ri'})
		for price in price_P:
			now_price = price.findAll('span',{'class':'price'})
			for real_name,raw_price in zip(name,now_price):
				print real_name.text,' -- ',raw_price.text
				query = '''insert into laptops(`Name and Model`,Price)value(%s,%s);''' %(real_name.text,raw_price.text)
				edit.execute(query)
conn.commit()
conn.close()
