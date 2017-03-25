from bs4 import BeautifulSoup
import requests

r_url = raw_input("site url:: ")
url = "http://" + r_url

r_data = requests.get(url)

r_html = r_data.text

html_data = BeautifulSoup(r_html,'html.parser')

for i in html_data.findAll('a'):
	print i.get('href')
