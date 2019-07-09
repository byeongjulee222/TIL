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