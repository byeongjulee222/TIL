import requests
from flask import Flask, render_template, request


app = Flask(__name__)

# 1. 로또 회차와 내 번호 입력 페이지

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

# 2. 결과 페이지

@app.route('/lotto_result')
def lotto_result():
    # 회차 번호를 받아온다.
    num = request.args.get('num')
    # 동행복권에 요청을 보내 응답을 받는다.
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
    # 우리가 크롬에서 보는 결과와 동일한 json 형식으로 변형 .json()
    lotto = res.json()

    # 그 회차의 당첨번호 6개만 가져오기
    winner = []
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])  # 리스트에 항목 추가

    # 내 번호 리스트 만들기
    numbers = []            # 단순 문자열에서 리스트화 (winner도 리스트 형식이기 때문에 맞춰줘야 함)
    my_numbers = request.args.get('numbers').split()    # 입력하는 항목을 띄어쓰기로 구분
    for num in my_numbers:
        numbers.append(int(num))

    # 등수 가리기(몇 개 맞았는지 교집합을 찾아야한다.)
    matched = 0     # 초기값을 0으로 설정하고 이후에 리스트 돌면서 조건 만족하면 +1 해주는 방식
    # 내 번호 요소를 뽑아서 당첨번호 리스트에 있는지 확인
    for num in numbers:
        if num in winner:
            matched += 1

    # set의 교집합을 이용하면
    matched = len(set(winner) & set(numbers))       # 위의 세줄짜리 for문과 동일 (set 연산자를 사용해서 교집합 활용)

    if len(numbers) == 6:       # 우리가 찍은 번호가 6개일 때만 진행
        if matched == 6:
            result = '1등입니다!'
        elif matched == 5:
            if lotto['bnusNo'] in numbers:      # 일단 5개를 맞추고 + 보너스 번호까지 만족할 때 (elif 안에 if)
                result = '2등입니다!'
            else:
                result = '3등입니다!'
        elif matched == 4:
            result = '4등입니다!'
        elif matched == 3:
            result = '5등입니다!'
        else:
            result = '꽝입니다!'
        return render_template('lotto_result.html', winner=winner, numbers=numbers, result=result)
    else:
        result = '번호의 수가 6개가 아닙니다.'


# int, string, list, dict, set

# set : 집합연산자
# 합집합, 교집합, 차집합

