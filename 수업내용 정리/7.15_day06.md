[TOC]

# 7/15 6일차

## 스케줄

- 매주 금요일 프로젝트 날
  - 4일간 배운 내용으로 프로젝트
  - 명세서(필수사항/선택사항)

## 2주후

- 월화(알고리즘)
- 수목금(준호쌤)



## 

- flask : 휘발성
- SQL : 저장, 기록



### 프레임워크 종류

앵귤러(구글)

Vue.js 

- 프론트엔드 전용

리액트

- 페이지를 새로고침하지 않고 게시물이 업로드되는 방식에 사용 (ex. 페이스북 타임라인)

-----리뷰 끝-----

---





## Python

개발자 : Guido van Rossum

### 1. 특징

- 단순하다
- 강력하다 (넓은 오픈소스)
- 빠르다 (학습하기, 개발속도)



Sublime Text : VS Code에 비해 가볍고 빠르다. 빠른 확인이 필요할 때 사용

- 추가적으로 설치해도 유용함.

Brackets : 프론트엔드 개발자들이 주로 사용



Jet Brain - IDE 프로그램을 다수 보유한 업체



### jupyter 사용

#### 1. git bash에서 pip install jupyterlab

#### 2. python -m notebook



켜는 법

- git bash에서 jupyter notebook



git bash에서 단축키 만들기

- code ~/.bashrc

```python
export FLASK_ENV=development
alias jp="jupyter notebook"
```

- source ~/.bashrc

--> 이제 jp만 입력해도 jupyter notebook 입력한 것과 같은 결과가 나옴

- 수업자료 열때 
  - pull받는 폴더 -> TIL -> 01_python -> git bash here -> jp



### jupyter 참고사항



상태에 따라 명령어가 다르다.

- edit mode(초록색)
  - command mode에서 셀을 더블클릭or Enter 누르면 edit mode로 변경
  - ctrl + enter = 현재 셀 실행
  - shift + enter = 실행 + 다음 셀 선택(다음 셀 없으면 새로운 셀 생성) -->주로 사용
  - alt + enter = 실행 + 다음 셀 생성



- command mode(파란색)

  - shift + Enter 누르면 command mode로 변경
  - 'd'를 두 번 빠르게 누르면 선택된 셀 삭제
  - 'z' 누르면 실행 취소
  - 'a' 누르면 선택된 셀 위에 새로운 셀 생성
  - 'b' 누르면 선택된 셀 아래에 새로운 셀 생성
  - shift 누르고 위 아래로 이동하면 셀 여러개 선택
  - 명령어 입력하고 shift+enter 누르면 바로 아래에 결과값이 나온다
  - In [ ] : 괄호안

  - 무한루프에 빠졌을 때(In [*]) : 
  - Kernel  -> Restart & Clear Output -> Restart & Clear All Outputs
  - 'm' 누르면 마크다운 형식



- command mode에서 'h' 누르면 단축키 목록을 볼 수 있다.



### 프로그래밍 폰트 필요조건

- 고정폭
- Sans-serif
- 가독성과 명확한 구분 (소문자 l(엘), 대문자 I(아이) 등등)



#### Hack font 다운로드

- Hack font 검색 후 제일 위 (https://sourcefoundry.org/hack/)
- 다운로드(Windows)
- .exe 파일 다운로드 후 설치
- 크롬 -> 설정 -> font 검색 -> 글꼴 맞춤 설정 -> 고정폭 글꼴을 Hack
- VS Code -> 왼쪽아래 톱니바퀴 -> Settings -> font 검색 -> Font -> Font Family에서 맨 앞에 Hack 추가



jupyter extension

https://github.com/ipython-contrib/jupyter_contrib_nbextensions

```
pip install jupyter_contrib_nbextensions
```

```
jupyter contrib nbextension install --user
```

jupyer -> Nbextensions 에서 Table of contents 체크



