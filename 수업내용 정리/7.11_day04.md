[TOC]

# 7/11_4일차

## 1. html 연결, 출력 예제

### 1.1 Hello World 

#### app.py)

```python 
@app.route('/') 
def hello():
    # return 'Hello World!'
    return render_template('index.html')    # 존재하지 않으니 우리가 만들어줘야 함
```

#### index.html)

```python
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>HELLO WORLD!</h1>
</body>
</html>
```

### 1.2 /greeting/<name (주소 뒤에 입력되는 값이 변경될 때)

app.py)

```python
from flask import Flask, render_template
app = Flask(__name__)		#싱글모듈 사용할 때 입력해야 하는 값

@app.route('/greeting/<name>')
def greeting(name):
    # return f'반갑습니다! {name}'
    return render_template('greeting.html', html_name=name)   # 오른쪽에서 왼쪽으로 값을 입력
```

greeting.html)

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <!-- 병주라는 이름으로 값이 오면 인사하고 아니면 누구세요라고 묻는다-->
    <!-- jinja 템플릿에서는 if문 끝에 닫아줘야됨-->
    <!-- 주석 안에 중괄호 넣으려면 	{##} 이런식으로 넣어야됨-->
    {% if html_name == '병주' %}    <!-- 사용자에게 보이지 않는 수식을 넣을 때 사용-->
        <h2>{{ html_name }} 왔니?</h2>
    {% else %}
        <h2>누구세요 ?</h2>
    {% endif %}
</body>
</html>
```

### 1.3 jinja2 개념잡기 (연산을 끝내고 html로 넘기기)

app.py)

```python
@app.route('/cube/<int:number>')
def cube(number):
    # 연산을 모두 끝내고 변수만 cube.html로 넘긴다.
    # return f'{number}의 세제곱은 {number**3}입니다.'
    result_num = number**3
    return render_template('calculate.html', result=result_num, number=number) # number에 입력하는 변수가 number로 이름이 같아도 된다.
    # app.py에서 계산한 결과값을 result와 number에 대입하여 calculate.html 변수에 대입
```

calculate.html)

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    {{number}}의 세제곱은 {{result}}입니다.
</body>
</html>
```





### cf) html 바로 출력

### 2.1 /ssafy

#### app.py)

```python
@app.route('/ssafy')        # http://127.0.0.1:5000/ssafy를 주소로 하는 서버 개설
def ssafy():
    return 'This is ssafy!'
```

### 2.2 /dday (날짜끼리 계산 )

#### app.py)

```python
@app.route('/dday')         # datetime 함수를 사용하려면 
    					    # from datetime import datetime 해줘야함
def dday():
    # 오늘 날짜
    today_time = datetime.now()
    # 수료 날짜
    endgame = datetime(2019, 11, 29)
    # 수료 날짜 - 오늘 날짜
    dday = endgame - today_time     # 날짜끼리 계산이 가능
    return f'{dday.days} 일 남았습니다.'
```

### 2.3 /html (헤드로 출력 연습)

#### app.py)

```python
@app.route('/html')
def html():
    return '<h1>This is HTML TAG</h1>'      # <h1> </h1> 안에 넣으면 head1 으로 출력
```

### 2.4 /html_line (여러줄 보내기 연습)

#### app.py)

```python
@app.route('/html_line')            
def html_line():                    
    return """
    <h1>여러 줄을 보내봅시다<h1>      
    <ul>
        <li>1번</li>
        <l1>2번</li>
    </ul>
    """
```

### 2.5  인원에 따라 메뉴 정하기

app.py)

```python
# /lunch/몇 명이 식사하는지 인원
# 플라스크는 여러 메뉴중에서 인원 수만큼의 메뉴를 응답합니다.

@app.route('/lunch/<int:people>')
def lunch(people):
    menu_list = ['rice', 'noodle', 'pizza', 'hamburger']   # 항목을 ''에 넣어줘야 함
    today_menu = random.sample(menu_list,people)           # random.sample(목록, 숫자)
    return f'{people}명이 식사할 메뉴는 {today_menu}입니다.' # return str(today_menu)도 가능
# 오류 뜨면 오류 읽어보고 수정가능
```



## 1. $ code ~/.bash_profile

export FLASK_ENV=development

```python
$ flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [11/Jul/2019 09:11:28] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [11/Jul/2019 09:11:28] "GET /favicon.ico HTTP/1.1" 404 -
```

이거 뜨면 환경(Environment를 변경해줘야 함)

순서 :

1. Terminal에서 flask 폴더로 위치 설정
2. code ~/.bash_profile
3. .bash_profile로 이동됨
4. source ~/.bash_profile
5. flask run 입력 후 Environment : development 확인

## 

### 2. variable routing(변수 라우팅)

라우팅(routing) : Internetwork을 통하여 근원지에서 목적지로 데이터가 전달될 수 있도록 하는 기능.

2.1 주소 뒤에 나오는 문자에 따라 출력값을 다르게

```python
@app.route('/greeting/<name>') # greeting/ 뒤에 나오는 문자에 따라 출력값이
def greeting(name):		       # 달라짐	<name> 앞에 string: 생략(기본값)
    return f'반갑습니다! {name}'
	return render_template('greeting.html', html_name=name)   # 오른쪽에서 왼쪽으로 값을 입력
```

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <!-- 병주라는 이름으로 값이 오면 인사하고 아니면 누구세요라고 묻는다-->
    <!-- jinja 템플릿에서는 if문 끝에 닫아줘야됨-->
    <!-- 주석 안에 중괄호 넣으려면 {##} 이런식으로 넣어야됨-->
    {% if html_name == '병주' %}    <!-- 사용자에게 보이지 않는 수식을 넣을 때 사용-->
        <h2>{{ html_name }} 왔니?</h2>
    {% else %}
        <h2>누구세요 ?</h2>
    {% endif %}

</body>
</html>
```



2.2 수료 날짜 d-day 계산 html 생성

```python
@app.route('/dday')
def dday():
    # 오늘 날짜
    today_time = datetime.now() # datetimet 함수를 사용하려면 
    							# from datetime import datetime 해줘야함
    # 수료 날짜
    endgame = datetime(2019, 11, 29)
    # 수료 날짜 - 오늘 날짜
    dday = endgame - today_time # 날짜끼리 계산이 가능
    return f'{dday.days} 일 남았습니다.'
```



###### cf) Git Bash

1. rm -rf ~/.bash_profile
2. code ~/.bashrc
3. source ~/.bashrc
4. git bash 켰을 때  warning : Found ~~/.bashrc 뜨고
5. ls -al 입력 후 



### render template

- 보통 template은 html 파일을 지칭

- templates 라는 폴더 안에서 사용자의 요구에 맞는 .html을 가져오는 작업

- app.py와 같은 위치에templates라는 폴더를 만들어야 함 (이름 끝에 's' 붙여야 함)

- templates 폴더 안에 

- flask 폴더에서 VS Code 열고

- 왼쪽 목록에서 flask 클릭 후 index.html 파일 생성

- VS Code 에서 ''! + tab' 누르면 html 기본 틀 생성됨

  ```python
  ### 실행전에 flask 폴더로 이동
  
  <!DOCTYPE html>
  <html lang="ko">  --> 한글을 기반으로 작성한다.
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>
  <body>
      <h1>HELLO WORLD!</h1>
  </body>
  </html>
  ```

- 작성 후 flask run 해보면 HELLO WORLD!가 입력된 html을 열어준다.



{{ }} : 변수로 인식



input text

input submit

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>

<body>
    <form action="/pong">			# 액션을 취하면 /pong으로 보낸다
        <input type="text" name="data"> # data라는 이름표를 달아준다 -> request.args.get('data')로 받아야함
        <input type="submit" value="퐁!!"> # input:submit 입력하면 "퐁!!"이라는 이름의 버튼을 만들어줌
    </form>
</body>
</html>
```

from flask import request 해서 request 명령어 받아와야됨



1. /ping
2. ping.html 응답
3. /pong 요청
4. pong.html 응답



[Flask] ping() / pong()

[Template] ping.html / pong.html



request.args로 바꾸고 ping에서 다시 입력하면 

ImmutableMultiDict([('data', 'dsa')])로 표시되고 형식이 Dict인 것을 알 수 있음.

---

### 3. ping - > pong

#### 	ping pong 순서

1. app.py에서

```python
@app.route('/ping')
def ping():
    return render_template('ping.html')
```

​	2. ping.html에서

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>

<body>
    <form action="/pong">			# 액션을 취하면 /pong으로 보낸다
        <input type="text" name="data"> # data라는 이름표를 달아준다 -> request.args.get('data')로 받아야함
        <input type="submit" value="퐁!!"> # input:submit 입력하면 "퐁!!"이라는 이름의 버튼을 만들어줌
</body>
</html>
```

#### 1. app.py

```python

@app.route('/pong')
def pong():
    print(dir(request))
    name = request.args.get('data')
    return render_template('pong.html', name=name)
```

#### pong.html

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>{{ name }} 받았음!</h1>
</body>
</html>
```



### Fake naver, Fake google







#### VonVon

#### insert

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="/personality">
        <input type="text" name="data"> 
        <input type="submit" value="입력">
    </form>

</body>
</html>
```

#### personality

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1> {{ name }} 님의 성격은!!!</h1>
    {{ personality[0] }} 한 스푼<br>
    {{personality[1]}} 두 스푼<br>
    {{personality[2]}} 으아아아<br>         <!-- <br> 입력하면 엔터-->
    
</body>
</html>
```

강사님 방법

```python
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>

<body>
  <h1>신이 {{ name }}님을 만들 때..</h1>
  <p>{{ first }} 한 스푼</p>
  <p>{{ second }} 두세 스푼</p>
  <p>{{ third }} 한 스ㅍ.. 으아아아아아아아악</p>
</body>

</html>
```



#### app.py

```python
@app.route('/insert')
def insert():
    return render_template('insert.html')


@app.route('/personality')
def personality():
    personalities = ['유쾌함', '활동성', '낭비벽', '물욕', '성실함']
    personality = random.sample(personalities, 3)
    name = request.args.get('data')
    return render_template('personality.html', name=name, personality=personality)

    # name을 변수로 입력해놓고 name=name을 적지 않음.
```

강사님 방법

```python
@app.route('/godmademe')
def godmademe():
    name = request.args.get('name')
    first_list = ['잘생김', '못생김', '어중간한']
    second_list = ['자신감', '쑥스러움', '애교', '잘난척']
    third_list = ['허세', '돈복', '식욕', '물욕', '성욕']
    
    first = random.choice(first_list)
    second = random.choice(second_list)
    third = random.choice(third_list)
    
    return render_template('godmademe.html', name=name, first=first, second=second, third=third)
```

dict['key']로 경우 key error가 발생



dict.get('key')로 가져올 경우 None 출력

#### Flask란?

- 파이썬으로 작성된 마이크로 웹 프레임 워크의 하나.
- WSGI(Web Server Gateway Interface) 마이크로 프레임 워크라고도 함.
- 특징
  - 다양한 웹 엔진과 붙어서 쓸 수 있으며, 가볍다
  - 코드가 비교적 단순하다
  - Django에 비해 최소한의 기능만을 제공(자유로운 어플리케이션 작성 가능)

#### WSGI란?

- 파이썬 스크립트가 웹 서버와 통신하기 위한 명세.(middle 웨어)

- 동작과정
  - 요청 -> 웹 서버 -> WSGI Server -> WSGI를 지원하는 웹 어플리케이션(Django, Flask 등)

#### jinja2란?

- Python용 템플릿 엔진
- Flask 웹 프레임워크에서 사용