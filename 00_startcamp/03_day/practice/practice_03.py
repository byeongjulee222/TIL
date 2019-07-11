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
    print("홀수")
else:
    print("짝수")