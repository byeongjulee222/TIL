[TOC]



# 7/16_day07

## 

#### o) 모음제거 연습문제

```python
my_str = "Life is too short, you need python"

##---방법 1---##
def remove_vowels(text):
    return ''.join(ch for ch in text if ch.lower() not in 'aeiou')
print(remove_vowels(my_str))


##---방법 2---##
for i in my_str:
    if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
        print(i, end='')


##---방법 3---##
# 그럼 하나하나씩 돌면서 모음이면 기록하지 않고, 모음이 아니면 기록해야겠다! -> 기록할 변수가 필요하네? -> result = ''
result = ''     # 빈 string을 만들고 문자열을 돌면서
for char in my_str:
# 모음이 아니면 기록
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
                result += char
print(result)
# 무식해보이지만 맞는 코드이다. 이렇게 단계별로 끊어서 생각하면 문제를 풀 수 있다.
# 아래 2가지 추가 풀이는 한 번에 접근해서 짤 수는 없다. 지금은 우선 위처럼 짜는게 우선이다.

##---방법 4---##
# 각각의 비교가 아니라, 어떤 통 안에 들어있나 없나를 판단
vowels = ['a', 'e', 'i', 'o', 'u']
vowels = 'aeiou'
result = ''
for char in my_str:
        if char not in vowels:
                result += char
print(result)

##---방법 5---##
# 새로운 변수를 만드는게 아니라 원본을 수정
vowels = 'aeiou'
for vowel in vowels:
        my_str = my_str.replace(vowel, '')
print(my_str)
```

