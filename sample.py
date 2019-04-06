from urllib.request import urlopen
from bs4 import BeautifulSoup

def find_title(detail_page):
    title = detail_page.find('h1', id="item_h1").find('span', {'itemprop':"name"}).get_text()
    return title

def find_inq_count(detail_page):
    count = detail_page.find('p', id='tabmenu_inqcnt').get_text()
    return count

def find_access_count(detail_page):
    count = detail_page.find('span', {'class':'ac_count'}).get_text()
    return count

def find_fav_count(detail_page):
    count = detail_page.find('span', {'class':'fav_count'}).get_text()
    return count

def find_price(detail_page):
    price = detail_page.find('div', id="priceWrap").find('span', {'class':'price_txt'}).get_text()
    return price

# html = urlopen('https://www.buyma.com/r/%E3%83%A2%E3%83%B3%E3%82%AF%E3%83%AC%E3%83%BC%E3%83%AB/')
html = urlopen('https://www.buyma.com/item/41422450/')
bs = BeautifulSoup(html.read(), 'html.parser')

print(find_title(bs),end=',')
print(find_inq_count(bs), end=',')
print(find_access_count(bs), end=',')
print(find_fav_count(bs), end=',')
print(find_price(bs), end=',')
print()
