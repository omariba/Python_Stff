from bs4 import BeautifulSoup
import requests

u_url = raw_input("enter url(without http://): ")
fin_url = "http://"+u_url

r_data = requests.get(fin_url)
html = r_data.text

print html
