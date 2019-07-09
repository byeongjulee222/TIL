import requests
from bs4 import BeautifulSoup

# 1. 원하는 주소로 요청을 보내 응답을 저장한다.
html = requests.get('https://finance.naver.com/sise/').text
# 2. 정보를 조작하기 편하게 바꾸고(정제)
soup = BeautifulSoup(html, 'html.parser')
# 3. 바꾼 정보 중 원하는 정보만 추출
kospi = soup.select_one('#KOSPI_now').text

print(kospi)