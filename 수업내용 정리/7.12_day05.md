[TOC]

# 7/12 5일차

## telegram 실습

### 전체 설정 과정

1. telegram_bot 폴더에서 git bash

2. app.py 파일 만들고

3. 시작 전에 서버 하나 열어두기

   ```python
   
   
   ​```python
   from flask import Flask
   
   app = Flask(__name__)
   
   @app.route('/')
   def hello():
       return 'Hi there!'
   ​```
   
   - 
   ```

   

4. telegram에서 botfather 검색 후 (체크 인증표시 확인) 시작

5. /newbot

6. juyahhh

7. juyahhh_bot  ---> 봇 이름 정하기

8. https://api.telegram.org/bot<token>/getUpdates

   입력 후 True 확인

   telegram에서 내 봇 친구추가 후

   웹에서 새로고침 ---> 봇이 받은 정보 모두 표시

9. 특정 사용자에게 메세지 보내기 (/sendmessage)

   1. 양식 : https://api.telegram.org/bot<token>/sendMessage?chat_id=<chat_id>&text=안녕하세요  //// 안에 토큰, 챗id 입력 후 이동

10.  vs code에서 send_message.py 만들고

11.  terminal에서 pip install python-decouple --> 따로 숨김파일을 설정해서 값을 가져옴
12. .env 파일 작성 (이 파일에서는 모두 대문자, 띄어쓰기X)



sendmessage :

```cmd
Session Status                online
Session Expires               7 hours, 59 minutes
Version                       2.3.30
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://60e91627.ngrok.io -> http://localhost:5000
Forwarding                    https://60e91627.ngrok.io -> http://localhost:5000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

#### webhook 등록주소

https://api.telegram.org/bot<token>/setWebhook?url=<ngrok-forwarding-http-url>

###  전체 app.py 코드

```python
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
    from_telegram = request.get_json()

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
            text = papago_res.json().get('message').get('result').get('translatedText')     #여기에 한/영 번역 텍스트가 있다.
            
        elif text[0:4] == '/한스 ':
            headers = {
                'X-Naver-Client-Id' : naver_client_id,
                'X-Naver-Client-Secret' : naver_client_secret
            }
            data = {'source': 'ko', 'target': 'es', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')     #여기에 한/영 번역 텍스트가 있다.

        elif text[0:4] == '/스한 ':
            headers = {
                'X-Naver-Client-Id' : naver_client_id,
                'X-Naver-Client-Secret' : naver_client_secret
            }
            data = {'source': 'es', 'target': 'ko', 'text': text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')     #여기에 한/영 번역 텍스트가 있다.

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


```



#### cf) Telegram 일반 정보

- All queries to the Telegram Bot API must be served over HTTPS and need to be presented in this form: 
  - http X  , https O
- telegram은 get, post  두가지 방식 모두 제공
- get 방식 - 입력하는 값이 외부로 노출됨
- post 방식 - 입력하는 값이 외부로 노출되지 않음

- https://api.telegram.org/bot + 토큰값 / method_이름 

- ngrok - 개방 포트 (서버 개방, 다른 사람도 신호를 보낼 수 있게)
  - ngrok.com 들어가서 다운로드

- 배포(deploy) - pythonanywhere