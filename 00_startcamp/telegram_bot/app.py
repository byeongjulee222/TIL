from flask import Flask, render_template, request
import requests
from decouple import config
import random

app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')

@app.route('/')
def hello():
    return 'Hi there!'

@app.route(f'/{token}', methods=['POST'])
def telegram():
    # step 1. 데이터 구조 print 해보기
    from_telegram = request.get_json()  # 우리가 볼 수 있는 json 형식으로 변환
                                        # Json : JavaScript Objec Notation
    if from_telegram.get('message') is not None:
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
        # 한글 키워드 받기

        # '/번역 '으로 입력이 시작된다면, 파파고로 번역이 동작한다.
        if text[0:4] == '/한영 ':
            headers = {
                'X-Naver-Client-Id' : naver_client_id,
                'X-Naver-Client-Secret' : naver_client_secret
            }
            data = {'source': 'ko', 'target': 'en', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')     #여기에 한/영 번역 텍스트가 있다.
    
        elif text[0:4] == '/영한 ':
            headers = {
                'X-Naver-Client-Id' : naver_client_id,
                'X-Naver-Client-Secret' : naver_client_secret
            }
            data = {'source': 'en', 'target': 'ko', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')    
            
        elif text[0:4] == '/한스 ':
            headers = {
                'X-Naver-Client-Id' : naver_client_id,
                'X-Naver-Client-Secret' : naver_client_secret
            }
            data = {'source': 'ko', 'target': 'es', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')     

        elif text[0:4] == '/스한 ':
            headers = {
                'X-Naver-Client-Id' : naver_client_id,
                'X-Naver-Client-Secret' : naver_client_secret
            }
            data = {'source': 'es', 'target': 'ko', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')    

        elif text[0:4] == '/한베 ':
            headers = {
                'X-Naver-Client-Id' : naver_client_id,
                'X-Naver-Client-Secret' : naver_client_secret
            }
            data = {'source': 'ko', 'target': 'vi', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')    

        elif text[0:4] == '/베한 ':
            headers = {
                'X-Naver-Client-Id' : naver_client_id,
                'X-Naver-Client-Secret' : naver_client_secret
            }
            data = {'source': 'vi', 'target': 'ko', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')    



        # 로또 당첨번호 봇
        if text[0:4] == '/로또 ':
            # 회차 번호를 받아온다.
            num = text[4:]
            # 동행복권에 요청을 보내 응답을 받는다.
            res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
            # 우리가 크롬에서 보는 결과와 동일한 json 형식으로 변형 .json()
            lotto = res.json()

            # 그 회차의 당첨번호 6개만 가져오기
            winner = []
            for i in range(1,7):
                winner.append(lotto[f'drwtNo{i}'])
            bonus_num = lotto['bnusNo']
            text = f'로또 {num}회차의 당첨번호는 {winner}입니다. 보너스 번호는 {bonus_num}입니다.'

        num_list = random.sample(range(1, 46), 6)
        if text[0:5] == '/로또추천':
            text = f'로또 추천 번호는 {sorted(num_list)}입니다.'
            print(text)

        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

    return '', 200