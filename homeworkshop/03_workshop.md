```python
# 단어를 입력 받아서
# if문으로 앞뒤가 같은지 판단하고
# True / False 반환
#----내가 푼 방식----#
word = input()

for i in range(len(word)):
        if word[i] == word[-(i+1)]:  # 0번째 = -1번째, 1번째 = -2번째, ...[i]=[-(i+1)]
                print(True)
                break
        else:
                print(False)
                break

#----강사님 방식----#
# 짝수 - NAAN
def is_palindrome(word):
        list_word = list(word) # ['N', 'A', 'A', 'N']
        # 리스트 요소의 양쪽 끝끼리 계속 비교하면서 진행
        for i in range(len(list_word) // 2):  # 2
                if list_word[i] != list_word[-i-1]:
                        return False
        return True
# 홀수일 때에도 만족

#----강사님 방식2----#
word = 'appa'
word == word[::-1]
```

