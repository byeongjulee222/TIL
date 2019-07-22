1. 

- Local scope: 정의된 함수
- Enclosed scope: 상위 함수
- Global scope: 함수 밖의 변수 혹은 import된 모듈
- Built-in scope: 파이썬안에 내장되어 있는 함수 또는 속성



2. (1)

- 2개를 리턴하는 것처럼 보이지만 실제로는 튜플 1개가 리턴되는 것이고, 이는 하나의 튜플 객체입니다.



cf)

□ 인자(Parameter) = 매개변수 = 가인수(Dummy argument)

○ 함수에 제공되는 데이터를 가리키는 변수

○ 인수를 담는 변수

○ int function(char aaa, int bbb) {} 에서 char aaa와 int bbb가 인자(=매개변수)



□ 인수(Argument) = 전달인자

○ 함수 호출 시 전달되는 값

○ int a = function(var1, "next", 15)에서 var1, "next", 15가 인수(=전달인자)



3. 

장점 : 1. 알고리즘 자체가 재귀적인 표현이 자연스럽다.

​		   2. 재귀 호출은 변수 사용을 줄여줄 수 있다.

단점 : 1. 함수의 인자값이 큰 수일 때 실행시키면 로딩 시간이 길다.