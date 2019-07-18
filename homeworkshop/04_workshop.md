```python
import math
# num이 a제곱과 b제곱 사이에 있다
# num의 제곱근은 a와 b 사이에 있다
# a-b의 제곱 값이 num보다 작으면 왼쪽 / 크면 오른쪽에 위치하여 계속 반복

# 비교하는 양쪽 수의 제곱값이 num에 가까워지도록

# mn = bn - sn
# mn**2 > sn
#   bn = mn
# mn**2 < sn

# def root(num):
#     sn = num - 1
#     bn = num

#     while bn - sn > 0.000000000001:
#         mn = (bn + sn) / 2
#         if mn**2 > num:
#             bn = mn
#         elif mn**2 < num:
#             sn = mn
#     return bn

# print(root(2))

# 강사님 방법

# 양의 정수 n을 입력받아 제곱근의 군사값(제곱했을 때 n이 되는 수)를 반환하는 함수를 작성.
# def my_sqrt(n): # n을 2라고 생각하고 논리식 진행
#     x, y = 1, n
#     result = 1  # 근사치 시작값 설정

#     # 제곱근의 제곱(result**2)과 입력값(n=2)의 차이가 적어도 이정도 차이보다 작아지면!
#     while abs(result**2 - n) > 1e-10:
#         result = (x+y)/2    # 양쪽 끝 값들을 더해서 2로 나눈다(절반을 구한다.)
#         # 위 근사치에 따라 x 또는 y의 값을 바꾼다.
#         if result**2 < n:
#             x = result
#         else:
#             y = result
#     return result

# print(my_sqrt(2))


def my_sqrt(n): # n을 2라고 생각하고 논리식 진행
    x, y = 1, n
    result = 1  
    # isclose 함수를 사용한 식 // 실수를 계산할 때 차이가 이정도면 차이가 없는거라 그냥 같다고 보자!
    # import math 필요함
    while not math.isclose(result**2, n):
        result = (x+y)/2    # 양쪽 끝 값들을 더해서 2로 나눈다(절반을 구한다.)
        # 위 근사치에 따라 x 또는 y의 값을 바꾼다.
        if result**2 < n:
            x = result
        else:
            y = result
    return result

print(my_sqrt(2))
```

