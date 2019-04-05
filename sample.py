from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.buyma.com/r/%E3%83%A2%E3%83%B3%E3%82%AF%E3%83%AC%E3%83%BC%E3%83%AB/')
bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.h1)


