[TOC]

# Web_190731

## Web이란?

- Wolrd Wide Web의 줄임말.
- Web Browser(클라이언트) ------ Web Server(서버)
- 클라이언트에서 요청 보내고 서버에서 응답받는 과정



- 주소 == IP 주소
- 도메인 == 상호명



Static web : 들어갈 때마다 자료가 일정하다 (댓글 기능이 없는 블로그, 학교 메인 페이지, github.io)

Dynamic web : 사용자가 수정하면 페이지가 고쳐져서 보여짐 (댓글)



- ##### URI, URL?

  - URI가 URL을 포함하는 개념



## HTML

- https (HyperText Transfer Protoco, 서버 통신 규약)
  - s : secure

- html (HyperText Markup Language, 마크업 언어)

- http vs https 속도?
  - https가 상위버전이고, 보안, 속도면에서 좋다.



- ##### Web

  - HTML (구조)
  - CSS (꾸밈)
  - JavaScript (활기)





- ##### W3C / WHATWG

  - WHATWG에서 개발하고 W3C에서 승인하는 형태 (과거)
  - WHATWG에서 자체적으로 HTML Living Standard 발표할 예정 



- #### Explorer 쓰지 않는 이유?

  1. 웹 표준을 지키지 않음
  2. 모바일 대응하지 않음
  3. 성능 개선 X
  4. 느림

  모든 사용자가 같은 브라우저를 사용하는게 아니기 때문에 IE에도 어느정도 대응을 해야함.

  -> Cross Browsing (서로 다른 OS 또는 플랫폼에서 인터넷이 이상 없이 구현되는 기술.)





##### 



#### Open Graph (OG)

- 링크를 붙여넣었을 때 미리보기 창을 함께 보내는 기능.
- 페이스북에서 개발
- head에서 작성



#### Style Guide (서로 보기 편하게 약속)

1. 들여쓰기 공백 2칸 설정

ctrl + shift + p

open settings json

```python
    "[html]": {
        "editor.tabSize": 2
    },
    "[css]": {
        "editor.tabSize": 2
    }
```

ctrl + shift + p

using tab --> 2 설정



2. 속성값에서 따옴표는 큰 따옴표로

3. 태그, 속성, 속성값 등에는 모두 소문자를 사용

4. 최상위 html 태그에는 lang 속성을 주어 문서의 기본 언어를 지정한다.(스크린리더는 lang을 통해 언어를 인식하여 자동으로 음성을 변환하거나 해당 언어에 적합한 발음을 제공)

5. IE는 특정 META 태그를 사용해 페이지가 특정 버전에 맞게 세팅 되도록 지정해준다.

```python
<meta http-equiv="X-UA-Compatible" content="ie=edge">
```

6. '=' 앞, 뒤에 띄우지 않는다.
7. boolean 속성 값은 따로 명시하지 않는다. (True 적지 않는다.)

8. 어떤 데이터를 불러올 때 보여줄 값이 없더라도 비우지 말고 alt="#" 입력

```python
<img src="https://picsum.photos/200" alt="#">
```





### DOM(Document Of Model) Tree

: 문서의 각 부분들을 객체로 표현한 API

주석 : `<!--  -->` or `ctrl + /`



시맨틱 태그

- <head>, <footer> ,...

- head 자리에 footer 내용 써도 에러나지 않음.
- but <head>에 추가해야 검색했을 때 내용이 함께 검색됨.
- 특별한 기능이 있는 것이 아니라 구분하기 위한 용도





- web developer 확장 프로그램 추가
- information - view document outline





##### Extensions

1. open in browser 추가

   Alt + b

- 안되면 open in default



2. beautify 추가 (코드 자동 정렬)

   keyboard shortcuts -> beautify selection 더블클릭 -> 사용할 단축키 추가 -> Enter



#####  단축키

alt + 

alt + shift 위 아래

ctrl + alt 위 아래



##### 사용하다 모르겠으면

 구글에 'html + 내용'으로 검색하고 w3school 사이트에서 확인



##### cf) 브라우저 점유율 비교

 (http://gs.statcounter.com/)



예제 조건

1. 새로고침 했을 때 첫번째 radio 버튼이 자동 클릭
2. 사이즈 선택 시 15와 30만 입력 가능 (타입 : 숫자)
3. 빵 선택시 플랫브레드는 선택 불가능하게