from bs4 import BeautifulSoup
import requests

u_url = raw_input("Input the website to get the headline: ")
print "--------------------------------------------------"
url = 'http://' + u_url
r_data = requests.get(url)

html = r_data.text

gold_mine = BeautifulSoup(html,'html.parser')

for i in gold_mine.findAll('h2'):
	fin = i.get_text()
	print fin
