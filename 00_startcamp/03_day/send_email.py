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