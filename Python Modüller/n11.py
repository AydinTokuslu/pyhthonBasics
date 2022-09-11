import requests
from bs4 import Beautifulsoup

url="https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html=requests.get(url).content
soup=Beautifulsoup(html, "html.parser")
print(html)
