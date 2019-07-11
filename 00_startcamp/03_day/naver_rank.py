import requests
from bs4 import BeautifulSoup

html = requests.get('http://www.naver.com').text
soup = BeautifulSoup(html, 'html.parser')

# searches = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')

# with open('naver_rank_list.txt', 'w',encoding='utf-8') as f:
#     for i in searches:
#         f.writelines(f'{i.text}\n')

# with open('~~~.txt','w',encoding='utf-8')as f:

# 요청 보내서 html 파일 받고

# BeautifulSoup으로  정제

# select method로 사용해서 list를 얻어낸다.

# 뽑은 list를 with 구문으로 잘 작성해보자.

# rank도 같이
searchings = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a')
# with open('naver_rank_list.txt', 'w',encoding='utf-8') as f:
#     for searching in searchings:
#         rank = searching.select_one('span.ah_r').text
#         keyword = searching.select_one('span.ah_k').text
#         f.write(f'{rank}위: {keyword}\n')
with open('naver_search.txt', 'w', encoding='utf-8') as f:
    for searching in searchings:
        rank = searching.select_one('span.ah_r').text
        keyword = searching.select_one('span.ah_k').text
        f.write(f'{rank}위: {keyword}\n')