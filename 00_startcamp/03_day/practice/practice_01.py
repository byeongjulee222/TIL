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