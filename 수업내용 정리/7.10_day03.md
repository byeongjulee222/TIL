[TOC]

# 7/10 (3일차)

## 1. 네이버 실시간 검색어를 스크래핑해서 txt 파일에 저장

### 1.1 파일 만들기

#### 1.1.1 파일 읽기

```python
# read() : 개행문자를 포함한 하나의 문자열
with open('with ssafy.txt', 'r') as f:
    all_text = f.read()                    # 박스(크기)를 지정
    print(all_text)

# readlines() : 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 list로 만들어 냄.
with open('with ssafy.txt', 'r') as f:
    lines = f.readlines()                   # 박스(크기)를 지정
    for line in lines:
        print(line)                         # 두 줄로 나오는 결과 --> 읽어오는 txt에 이미 \n이 있어서.
                                            # print(line.strip()) 입력해주면 \n 없이 출력됨.
        # print(dir(line))                  # dir() : ()안의 함수 뒤에 사용할 수 있는 명령어가 무엇인지 나열
```



#### 1.1.2 파일 쓰기

```python
# 변수에 만들고 싶은 파일을 open() 해야 한다.
# open() 할 때 r: 읽기 / w: 쓰기(+덮어쓰기) / a: 추가
# f = open('만들 파일 명', '행동')    # 파일 조작할 때 f 사용
# 메모장에 1~10까지 머리번호 입력

#----1----#
f = open('ssafy.txt', 'w')
for i in range(10):
    f.write(f'This is line {i+1}.\n')     # 여기에 글을 쓰겠다 // \n: next line의 약자
f.close()           # 끝나고 무조건 닫아줘야 함

#----2----#
# with 구문 (context manager)
with open('with ssafy.txt', 'w') as f:          # f를 변수로 쓰겠다
     for i in range(10):
         f.write(f'This is line {i+1}.\n')      # 안에 내용이 끝나면 스스로 실행을 멈춤.
                                                # open(~) 명령어보다 with 구문이 더 직관적이고 편하다.

#----3----#
# writelines() : list를 넣어주면, 요소 하나당 한 줄씩 작성
with open('ssafy.txt', 'w') as f:               # w가 덮어쓰기로 작용
    f.writelines(['0.\n', '1.\n', '2.\n', '3'])


# escape 문자
# \n : 개행문자(다음 줄 이동)
# \t : 탭문자
# \\ : 백슬래쉬를 사용하기 위해
# \' : 따옴표 사용
# \" : 쌍따옴표
```



#### 1.1.3 파일 뒤집기

```python
# DOCstring : 주석과 같은 효과
"""
이 함수는 블라블라
누가 만들었고
어떻게 사용하고
이런 함수입니다.
"""

"""
다음과 같은 내용의 파일 quest.txt 가 있다.
0
1
2
3

이 파일의 내용을 다음과 같이 역순으로 reverse_quest.txt 라는 파일로 저장하시오.
3
2
1
0

"""

# 1. 읽고
# 2. 뒤집고
# 3. 작성하기

#----1번째----#
with open('quest.txt', 'r') as f:
    all_text = f.readlines()
    
all_text.reverse()    # or all_text[::-1]

with open('reverse_quest.txt', 'w') as f: 
    f.writelines(all_text)                  # or for line in all_text:
                                            #        f.write(line)


#----2번째----#
# with open('quest.txt', 'r') as f:
#     all_text = f.read()

# with open('reverse_quest.txt', 'w') as f:
#     f.writelines(f'{all_text[::-1].strip()}\n')

#----3번째----#
# with open('quest.txt','r') as rf, open('reverse_quest.txt','w') as wf:
#     for line in reversed(rf.readlines()):
#         wf.write(line)
```

### 2. 스크래핑

```python
import requests
from bs4 import BeautifulSoup

html = requests.get('http://www.naver.com').text
soup = BeautifulSoup(html, 'html.parser')

searches = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')

with open('naver_rank_list.txt', 'w',encoding='utf-8') as f:
    for i in searches:
        f.writelines(f'{i.text}\n')

# with open('~~~.txt','w',encoding='utf-8')as f:

# 요청 보내서 html 파일 받고

# BeautifulSoup으로  정제

# select method로 사용해서 list를 얻어낸다.

# 뽑은 list를 with 구문으로 잘 작성해보자.
```











---

### 보너스) 이메일 보내기

1. #### 여러 사람에게 보내기

```python
import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('PASSWORD : ')

to_email_list = ['dave.juya777@gmail.com', '91hongpie@gmail.com', 'toohong5@gmail.com']
for email in to_email_list:
    msg = EmailMessage()
    msg['Subject'] = '과제 제출'
    msg['From'] = 'tkwk3924@naver.com'
    msg['To'] = email
    msg.set_content('과제 보냅니다.')

ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
ssafy.login('tkwk3924', password)
ssafy.send_message(msg)

print('이메일 전송 완료!')
```

2. #### 메뉴 랜덤하게 보내기

```python
import random
import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('PASSWORD : ')

text = ['치킨', '피자', '돈까스', '냉면']
menu = random.choice(text)

for menu in text:
    msg = EmailMessage()
    msg['Subject'] = '과제 제출'
    msg['From'] = 'tkwk3924@naver.com'
    msg['To'] = 'dave.juya777@gmail.com'
    msg.set_content(menu)

ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
ssafy.login('tkwk3924', password)
ssafy.send_message(msg)

print('이메일 전송 완료!')
```

---

#### 명령어 import 했을 때 사용법

1)

import bs4

soup = bs4.BeaSoup()



2)

from bs4 import BeaSoup

soup = BeaSoup()



## Cf) 연습문제

### 1. 문자열 첫 번째, 마지막 글자 출력

```python
'''
# 문제 1.
문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.
'''

str = input('문자를 입력하세요: ')

str = list(str)

first_letter = str[0]
last_letter = str[len(str)-1]

print(f'첫 글자: {first_letter}')
print(f'마지막 글자: {last_letter}')

# 다른 방법
print(f'첫 글자는 {str[0]}, 마지막 글자 {str[-1]}')
```

### 2. 1~N까지 한 줄에 하나씩 출력

```python
'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

numbers = int(input('숫자를 입력하세요: '))     # int를 씌워줘야 숫자로 인식

for i in range(1,numbers+1):
    print(i)
```

### 3.  홀,짝 구분

```python
'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('숫자를 입력하세요: '))

if number % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 다른 방법
if number % 2:
    print("홀수")  # 값이 있으면 홀수
else:
    print("짝수")  # 값이 없으면 짝수 (0도 값이 없는 것으로 인식)
```

### 4. 국영수과 점수 합,불

```python
'''
문제 4.
표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
국어는 90점 이상,
영어는 80점 초과,
수학은 85점 초과, 
과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)
다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 
'''

a = int(input('국어: '))
b = int(input('영어: '))
c = int(input('수학: '))
d = int(input('과학: '))

if a >= 90 and b > 80 and c > 85 and d >= 80:
    print(True)			# True, 'True' 둘다 가능
else:
    print(False)
```

### 5. 숫자 내림차순

```python
'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''
# 문자열 => 리스트로 형변환을 하는게 포인트!!!

#----1----#
# prices = input('물품 가격을 입력하세요: ')

# prices_list = prices.split(';')             # 목록의 값들을 ';'을 기준으로 나눔
#                                             # 실행 결과 : 리스트로 바뀜
# prices_list.sort(reverse=True)              # 목록의 배열을 내림차순으로
#                                             # sort 사용할 때 문자형을 숫자형으로 변경해야
#                                             # 크기별로 정렬이 가능하다

# for i in prices_list:                       
#     print(int(i))                     # 결과값이 세로로 출력


#----2----#
# prices = input('물품 가격을 입력하세요: ')

# prices_list = prices.split(';')

# prices_list.sort(reverse = True)

# print(prices_list)                  # 결과값이 리스트 형식으로 가로로 출력

#----3----#
# 빈 리스트를 먼저 만들어두고 풀이
prices = input('물품 가격을 입력하세요: ')
makes = prices.split(';')

boxes = []
for make in makes:
    boxes.append(int(make))
boxes.sort(reverse=True)

for box in boxes:
    print(box)


# append() : 리스트에 요소를 추가
# list.append(1) : 리스트에 1을 추가한다.
```



- Github에 사진 올리는 법

TIL -> issues -> new issues -> 이미지 드래그 앤 드랍 -> 출력된 주소를 markdown에 입력

```python
<!DOCTYPE html>  # html 만들때는 처음에 형식을 선언해줘야 함
<html> # 여는 태그
<head> # 사용자에게 안보이는 로딩 태그
    <meta charset="UTF-8">
    <title>여기는 네이버입니다.</title>
    <link rel="stylesheet" href="test/style.css"> # 위치는 자신의 위치를 기준으로 // 같은 폴더내에 있으면 바로 파일명만 입력
</head>
<body>
    <h1>H1 태그입니다.</h1>
    <h2>HTML & CSS 맛보기</h2>
</body>



</html> # 닫는 태그
```



## 2. Web 수정

### 2.1 terminal에 대한 설정을 변경하기 위한 과정

- .bash_profile  => 항상 ~/(home)에서 설정해야 한다.

- git bash에서 code ~/.bash_profile 입력

- VS Code에서 export FLASK_APP=hello.py 입력

- source ~/.bash_profile => 리셋하는 명령어 (설정 후 리셋해야 설정 완료)
  - flask run 입력 후 서버 열리는지 확인
- 서버에 접속하라 -> flask에 접속하라



### 2.2 수정사항 즉시 업데이트

- VS Code에서 export FLASK_ENV=development 입력
- 저장
- Terminal에서 source ~/.bash_profile 입력
- flask run 입력



### 2.3 url 여러개로

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')		# 입력하는 역할. Web에 신호를 전달
def hello():		# 함수명은 아무렇게나 정의해도 된다.
    return "Hello World!"

    # 127.0.0.1 : local host address

@app.route('/ssafy')# 입력하는 역할. Web에 신호를 전달
def bye():			# 두 번째 함수명은 첫 번째 함수명과 달라야 함.
    return "This is ssafy !"
```



### 2.4 css 수정

- css : 프론트엔드, 그래픽 담당