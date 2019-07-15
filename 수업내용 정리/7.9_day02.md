[TOC]

# 7/9 (2일차)

## 1. 인기검색어 순위표 크롤링

### 1.1 <.select>

- .select_one('경로')
- .select('경로') -> 리스트로 나온다.
- AttributeError: 'list' object has no attribute 'text' --> 
- select로 가져오면 리스트로 가져온다.
- '<span>~~<span>'
- ...
- 규칙 찾기 어려울 때 한 줄 작성하고 print()로 잘 실행되는지 확인
- 

```python
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(4) > a > span.ah_k
1. 이런 주소가 나올 때 규칙 파악
	-->li:nth-child(~) 반복되는 것 파악
	-->li 뒤에꺼 지우면 목록 형식으로 추출 가능

#######최종 명령어 목록#######
import requests
from bs4 import BeautifulSoup # bs4가 큰 모듈이기 때문에 모두 불러오게되면 실행 속도가 느려짐
# 그냥 import bs4 해도 상관없음

url = 'https://www.naver.com/'
html = requests.get(url).text # 주소를 텍스트 값으로 추출
soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup가 인식하는 모양으로 변경

searches = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(' & i & ') > a > span.ah_k')


for i in searches:   #for문으로 돌리기
    print(i.text)    #.text로 필요한 자료만 추출
```

## 2. GitHub

### 2.1 Git?

- (분산) 버전 관리 시스템
- 프로젝트 이전 버전을 복원하고 변경 사항을 비교, 분석 및 병합도 가능
- 수정할 때마다 어떤 것이 수정되었는지 확인 가능
- 현재 파일을 안전한 상태로 과거 모습 그대로 복원 가능
- add - 커밋할 목록에 추가
- commit - 커밋(create a snapshot) 만들기 --> 버전 도장찍기 (캡쳐 느낌)
- push - 현재까지의 역사(commits)가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기
- 한 번에 단계를 여러개 뛸 수 없다(jump 불가)

### 2.2 Github와 연결

- Git Bash에서 
- git config --global user.name "byeongjulee222"
- git config --global user.email dave.juya777@gmail.com
- git config --global --list  : 연결된 목록 출력



- git init
  -  : 해당 폴더를 추적할 수 있도록 권한 부여, 저장소 설정 (가장 먼저 해줘야 함) (* 가장 최상위 폴더(TIL)에서 설정해줘야 함)

---> (master) 표시 뜨면 git 권한내에 있다는 뜻 (master : git 처음 만든 사람)

- git status : git 현재 상태 표시 명령어 (*자주 확인해야 함)
- git add 00_startcamp/
  - git에 add 해줘야 git이 권한을 가짐



- 집에서 할 때는
  - git clone
  - git init
  - git pull
  - git add, commit, push

### 2.3 Git ignore(*)

#### 2.3.1 git ignore?

		-	git에 올라가면 안되는 내용(개인정보, 토큰...)이 올라가지 않도록 설정
		-	첫 push전에 ignore 설정해야함 (*)
		-	숨겨진 파일 중 .git : git init을 통해 git 연결했던 내용

#### 2.3.2 작성 방법

​	https://github.com/github/gitignore/blob/master/Python.gitignore

or gitignore.io에서 사용할 언어 선택 후 검색

복, 붙



명령문 전체 복사해서

.gitignore에 붙여넣기 후 저장



## 3. 문자열(string) 삽입

### 3.1 '문자열' '12'

#### 3.1.1 터미널 위치 현재위치로 설정하는 단축키 추가

- Extensions 들어가서  'Terminal Here' install
- ctrl + shift + p 누르고 오른쪽 키보드 모양 누르고 'ctrl + `' 검색
- 기존에 있던 단축키 내용 삭제
- 키보드 모양 해제하고 'terminal here' 검색해서 단축키 추가

### 

## 4. 파일명 변경

### 4.1 바꾸는 과정

- os를 import 한다 (import os)
- 해당 폴더로 들어간다 (os.chdir(r'주소'))   --> ('주소' : 파일 위치)
  - '주소'앞에 r 써줘야 window에서 '주소' 내용 중 \를 escape로 인식 안하고 주소 그대로 인식함.
- 폴더 안의 모든 파일 이름을 수집  os.listdir('.')

- 각각의 파일명을 돌면서 수정  os.rename(이전 파일명, 바꿀 파일명)



### 4.2 수정

- SAMSUNG -> SSAFY
- os.rename(이전 파일명, 이전 파일명.replace('교체되어야 할 문자열', '새로 입력될 문자열'))



## 5. f string 활용법

#### 5.1 f_string

```python
name = '이병주'
greet = '안녕하세요'
last_message = '입니다.'

print(f'{greet}, {name}{last_message}')

# 점심 메뉴 추천
import random

menu = ['돈까스', '짬뽕', '볶음밥']
lunch = random.choice(menu)

print(f'오늘의 점심은 {lunch}입니다.')

# 로또 추천
numbers = range(1, 46)
lotto = random.sample(numbers, 6)

print(f'오늘의 로또 당첨 번호는 {sorted(lotto)}입니다.')

# 필요하면 이렇게도 해보자
name = '홍길동'
print('안녕하세요, ' + name + '입니다.')
```



** 추천 사이트

1. 코딩도장 (초심자용)
2. 파이썬 도큐먼드 (정석)

3. 책 : 러닝 파이썬 상. 하편(알고리즘 풀다가 파이썬 실력이 수직상승할 때)