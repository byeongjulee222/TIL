from flask import Flask, render_template, request        # from ~ import 여러개 가능
from datetime import datetime
import random
app = Flask(__name__)       # 싱글모듈 사용할 때 입력해야 하는 값

@app.route('/') 
def hello():
    # return 'Hello World!'
    return render_template('index.html')    # 존재하지 않으니 우리가 만들어줘야 함


@app.route('/ssafy')        # http://127.0.0.1:5000/ssafy를 주소로 하는 서버 개설
def ssafy():
    return 'This is ssafy!'


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


@app.route('/html')
def html():
    return '<h1>This is HTML TAG</h1>'      # <h1> </h1> 안에 넣으면 head1 으로 출력


@app.route('/html_line')            
def html_line():                    
    return """
    <h1>여러 줄을 보내봅시다<h1>      
    <ul>
        <li>1번</li>
        <l1>2번</li>
    </ul>
    """

@app.route('/greeting/<name>')
def greeting(name):
    # return f'반갑습니다! {name}'
    return render_template('greeting.html', html_name=name)   # 오른쪽에서 왼쪽으로 값을 입력


# jinja2 개념잡기
@app.route('/cube/<int:number>')
def cube(number):
    # 연산을 모두 끝내고 변수만 cube.html로 넘긴다.
    # return f'{number}의 세제곱은 {number**3}입니다.'
    result_num = number**3
    return render_template('calculate.html', result=result_num, number=number) # number에 입력하는 변수가 number로 이름이 같아도 된다.
    # app.py에서 계산한 결과값을 result와 number에 대입하여 calculate.html 변수에 대입

# /lunch/몇 명이 식사하는지 인원
# 플라스크는 여러 메뉴중에서 인원 수만큼의 메뉴를 응답합니다.

@app.route('/lunch/<int:people>')
def lunch(people):
    menu_list = ['rice', 'noodle', 'pizza', 'hamburger']   # 항목을 ''에 넣어줘야 함
    today_menu = random.sample(menu_list,people)           # random.sample(목록, 숫자)
    return f'{people}명이 식사할 메뉴는 {today_menu}입니다.' # return str(today_menu)도 가능
# 오류 뜨면 오류 읽어보고 수정가능


# 영화 목록 보여주는 페이지 만들기
@app.route('/movie')
def movie():
    movies = ['어벤져스:엔드게임', '도어락', '기생충', '알라딘']
    return render_template('movies.html', movies=movies)

### Flask Request & Response ###
# ping.html / pong.html

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    print(dir(request))
    name = request.args.get('data')
    return render_template('pong.html', name=name)


# https://search.naver.com/search.naver?query=

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')


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