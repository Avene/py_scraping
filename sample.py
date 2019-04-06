import sys
import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import time

def get_top_product_links(keyword):
    url = 'https://www.buyma.com/r/' + keyword
    html = urlopen(url)
    bs = BeautifulSoup(html.read(), 'html.parser')
    products = bs.find_all('div', {'class':'product_name'})
    links = ['https://www.buyma.com' + product.find('a', {'data-action':'view_item'}).attrs['href'] for product in products]
    return links
    
def find_title(detail_page):
    title = detail_page.find('h1', id="item_h1").find('span', {'itemprop':"name"}).get_text()
    return title.strip().replace(',', '')

def find_inq_count(detail_page):
    count = detail_page.find('p', id='tabmenu_inqcnt').get_text()
    return count.strip().replace(',', '')

def find_access_count(detail_page):
    count = detail_page.find('span', {'class':'ac_count'}).get_text()
    return count.strip().replace(',', '')

def find_fav_count(detail_page):
    count = detail_page.find('span', {'class':'fav_count'}).get_text()
    return count.strip().replace(',', '')

def find_price(detail_page):
    price = detail_page.find('div', id="priceWrap").find('span', {'class':'price_txt'}).get_text()
    return price.strip().replace(',', '')

def find_brand(detail_page):
    brand = detail_page.find('dl', id="s_brand").find('a', itemprop="brand").get_text()
    return brand.strip().replace(',', '')

def print_header():
    print('timestamp, rank, brand, title, inqury, access, favorities, price')

def print_detail(bs):
    elements = [find_brand(bs),
                find_title(bs), 
                find_inq_count(bs), 
                find_access_count(bs),
                find_fav_count(bs),
                find_price(bs)]

    line = ','.join('"{0}"'.format(w) for w in elements)
    print(line)

keyword = sys.argv[1]
links = get_top_product_links(urllib.parse.quote(keyword))

print_header()
for i in range(len(links)):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('"%Y-%m-%d_%H:%M:%S"')
    detail_page = urlopen(links[i])
    detail_obj = BeautifulSoup(detail_page.read(), 'html.parser')
    print(timestamp, end=',')
    print(i + 1, end=',')
    print_detail(detail_obj)
