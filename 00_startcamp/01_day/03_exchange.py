import requests
from bs4 import BeautifulSoup

html = requests.get('https://finance.naver.com/marketindex/') # 정보 가져옴

soup = BeautifulSoup(html, 'html.parser') # 정보 가공
exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text # 필요한 정보만 빼냄
print(exchange)