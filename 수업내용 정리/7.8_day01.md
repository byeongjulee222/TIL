[TOC]

# 7/8 1일차

## 1. 

- 인공지능 스피커 - 데이터 수집

- 차세대 인터페이스 -> 음성인식

- dictionary
  - "견출지 붙인 박스들의 묶음"

- dust = {"영등포구" : 58, "강남구" : 40} -- 중괄호



## 2. bash

### 2.1 기본 명령어

- ctrl + l : 명령줄 제일 위로

- 단어 누르다 tab 누르면 자동완성
- 항상 작업 위치 확인 (ls)
- 버전확인 : python -V (대문자)

### 2.2 Git bash 설치 순서

- git bash - git for windows 다운로드

Use Vim

2. python
Add Python 3.7 to PATH 체크
Disable~~ 누르고 close
2. vscode
  download for windows
  "Code로 열기~~ 2개 체크
  ctrl + shift + p -> select command shell -> Git Bash
  View -> Termial 눌렀을 때 Git Bash랑 같으면 설정완료
  - 기본 명령어
    - ctrl + ~ : 터미널  on/off
      3. 왼쪽 밑에 Extension 눌러서 파이썬 추가
         ctrl + / : 주석처리

VS Code 
1)
import webbrowser

### 1. 한번에 여러개의 웹 사이트 열기
web_list = ['www.naver.com', 'www.google.com', 'www.youtube.com']   --> 변수 정의할 때 list, dict,.. 등등은 사용하면 안됨

```python
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
```

### 2. 환율 정보 받아오기
```python
import requests
from bs4 import BeautifulSoup

# 1. 원하는 주소로 요청을 보내 응답을 저장한다.
html = requests.get('https://finance.naver.com/sise/').text
# 2. 정보를 조작하기 편하게 바꾸고(정제)
soup = BeautifulSoup(html, 'html.parser')
# 3. 바꾼 정보 중 원하는 정보만 추출
kospi = soup.select_one('#KOSPI_now').text

print(kospi)
```

### 3. 환율 정보 받아오기

```python
import requests
from bs4 import BeautifulSoup

html = requests.get('https://finance.naver.com/marketindex/') # 정보 가져옴

soup = BeautifulSoup(html, 'html.parser') # 정보 가공
exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text # 필요한 정보만 빼냄
print(exchange)
```



///Git Terminal

python 01_auto_browser.py
history --> 명령어 입력했던 기록 나열

*** pip --> 파이썬 패키지 관리자
pip install requests ---> 패키지 다운로드

pip install bs4 --> BeautifulSoup 다운로드

BeautifulSoup(a,b) --> a를 b로 가공

웹에서 필요한 정보 위치 출력 : ctrl + shift + i --> copy --> copy selector

///Typora 다운로드