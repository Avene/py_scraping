import sys
import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_top_product_links(keyword):
    url = 'https://www.buyma.com/r/' + keyword
    html = urlopen(url)
    bs = BeautifulSoup(html.read(), 'html.parser')
    products = bs.find_all('div', {'class':'product_name'})
    links = ['https://www.buyma.com' + product.find('a', {'data-action':'view_item'}).attrs['href'] for product in products]
    return links
    
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

def print_header():
    print('title, inqury, access, favorities, price')

def print_detail(bs):
    print(find_title(bs),end=',')
    print(find_inq_count(bs), end=',')
    print(find_access_count(bs), end=',')
    print(find_fav_count(bs), end=',')
    print(find_price(bs), end=',')
    print()

links = get_top_product_links(urllib.parse.quote(sys.argv[1]))
links = links[0:5]
print(len(links), 'items found')
detail_pages = [urlopen(link) for link in links]
detail_bs_objs = [BeautifulSoup(detail.read(), 'html.parser') for detail in detail_pages]

print_header()
for detail_obj in detail_bs_objs:
    print_detail(detail_obj)