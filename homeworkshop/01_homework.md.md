01_homework.md



1. Python에서 사용할 수 없는 식별자(예약어)를 찾아 작성하세요.

```python
import keyword
print(keyword.kwlist)

False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```



2. 파이썬에서는 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다. (floating point rounding error) 따라서, 아래의 값을 비교하기 위해 작성해야하는 코드를 작성하세요.

```python
import math

math.isclose(a,b)
```



3. 이스케이프 문자열 중

```python
1) 줄바꿈  ->  \n

2) 탭  ->  \t

3) \  ->  \\
```



4. "안녕, 철수야"를 String Interpolation을 사용하여 출력하세요.

```python
name = "철수"
print(f'"안녕, {name}야"')
```



5. 다음 중 형변환시 오류가 발생하는 것은?

5)int('3.5')