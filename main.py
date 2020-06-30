import requests
from bs4 import BeautifulSoup

URL = 'http://web.archive.org/web/20050923194412/http://www.chara.gsu.edu/RECONS/TOP100.htm'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

text = (soup.get_text())
a = text.split('\n')
list_stars = []
for i in range(62, (len(a)-85)):
    list_stars.append((a[i]))
for elements in list_stars:
    a = elements.split("\t")
