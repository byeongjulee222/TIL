import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.naver.com/').text
soup = BeautifulSoup(html, 'html.parser')

searches = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(4) > a > span.ah_k')


for i in searches:   #for문으로 돌리기
    print(i.text)    #.text로 필요한 자료만 추출

# 두번째 커밋을 위한 주석!!!