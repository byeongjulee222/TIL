import webbrowser

# # 1. 리스트가 필요
# web_list = ['www.naver.com', 'www.google.com', 'www.youtube.com']


# 변수 정의할 때 list, dict와 같은 명령어와 겹치는 단어는 사용 안됨.
idols = ['bts', 'nrg', 'hot', 'babyvox']
url = 'https://search.naver.com/search.naver?query='

# 2. 반복문(for) 안에서 webbrowser.open() 이 실행
for idol in idols:
    webbrowser.open_new(url + idol)

# import requests

# response = requests.get('https://www.naver.com/').status_code # 네이버로부터 응답을 받는 명령어
# print(response)