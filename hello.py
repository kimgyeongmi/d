import requests
import bs4

URL = "https://browse.gmarket.co.kr/search?keyword=마스크"
raw = requests.get(URL)

html = bs4.BeautifulSoup(raw.text, 'html.parser')

box = html.find('div', {'class' : 'section__module-wrap', 'module-design-id' : '15'})

items = box.find_all('div', {"class" : 'box__item-container'})

print(len(items))