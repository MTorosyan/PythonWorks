#Create a script to
import requests
from bs4 import BeautifulSoup as bsoup

my_url = 'https://cex.io/bitcoin-calculator'
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(my_url)
soup = bsoup(page.text, "html.parser")

print(soup)
