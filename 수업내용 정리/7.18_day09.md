# 7.18 day_09

Python 스타일 가이드

참조 : https://python-guide-kr.readthedocs.io/ko/latest/writing/style.html 



```python
# parameter != argument (is로 비교했을 때에는 서로 다른 것이다)

# x == parameter(매개변수)
# 매개변수는 함수의 정의 부분에서 볼 수 있다.
def func(x):
    return x + 2

# 2 == argument(인자, 전달인자)
# 인자는 함수를 호출하는 부분에서 볼 수 있다.
func(2)
```

