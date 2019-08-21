# django imports style guide
# 1. standard library
# 2. third-party(ex.request)
# 3. Django(ex.from django import ~) 길이가 같다면 짧은 것을 위로
# 4. local django

import random
import requests
from pprint import pprint
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request): # 첫번째 인자는 반드시 request
    return render(request, 'pages/index.html') # render()의 첫번째 인자도 반드시 request


# view에서는 두 함수사이 간격을 두 줄로 한다.
def introduce(request, name, age):
    context = {'name': name, 'age': age,}
    return render(request, 'pages/introduce.html', context)


def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick}
    return render(request, 'pages/dinner.html', context)


def image(request):
    return render(request, 'pages/image.html')


def hello(request, name):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'name': name, 'pick': pick,}
    return render(request, 'pages/hello.html', context)


def times(request, number1, number2):
    result = number1 * number2
    context = {'result': result, 'number1':number1, 'number2':number2,}
    return render(request, 'pages/times.html', context)


def area(request, radius):
    result = 3.14 * (radius**2)
    context = {'result': result, 'radius': radius}
    return render(request, 'pages/area.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피',]
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'bean',]
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'pages/template_language.html', context)


def isitgwangbok(request):
    today = datetime.now()
    if today.month == 8 and today.day == 15:
        result = True
    else:
        result = False
    context = {'result': result, 'today': today,}
    return render(request, 'pages/isitgwangbok.html', context)


def throw(request):
    return render(request, 'pages/throw.html')


def catch(request):
    # pprint(request)
    # pprint(request.scheme)
    # pprint(request.path)
    # pprint(request.method)
    # pprint(request.GET)
    # pprint(request.META)
    # GET 안에 딕셔너리 형식의 데이터 내에서 원하는 값을 빼오기
    message = request.GET.get('message')
    context = {'message': message,}
    return render(request, 'pages/catch.html', context)


def art(request):
    return render(request, 'pages/art.html')


def result(request):
    # 1. art에서 form으로 보낸 데이터를 받는다.
    word = request.GET.get('word')

    # 2. ARTII API의 font list로 요청을 보내 응답을 text로 받는다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    # print(fonts)
    # 3. str을 list로 바꾼다. (랜덤으로 돌려서 폰트를 변경하기 위해)
    fonts = fonts.split('\n')

    # 4. fonts list 안에 들어있는 요소 중 하나를 선택해서 변수에 저장
    font = random.choice(fonts)

    # 5. 위에서 만든 word와 font를 가지고 다시 요청을 보내 응답 결과를 받는다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {'response': response,}
    return render(request, 'pages/result.html', context)


def user_new(request):
    return render(request, 'pages/user_new.html')


def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {'name': name, 'pwd': pwd,}
    return render(request, 'pages/user_create.html', context)


def static_example(request):
    return render(request, 'pages/static_example.html')