[TOC]

# 웹 정리

## HTML

- HyperText Markup Language

### HTML 요소

- `<html lang="ko">` : HTML 문서의 최상위 요소(문서의 root)
- head와 body로 구분



#### HTML로 표 만들기

- colspan="2" : 2개의 열을 차지할 것이다.
- rowspan="2" : 2개의 행을 차지할 것이다.



#### head 요소

- 문서 제목, 문자 코드와 같이 해당 문서 정보를 담고 있으며 브라우저에 나타나지 않는다.
- CSS 선언 or 외부 로딩 파일 지정 등도 작성

- cf) Open Graph 방식
  - 사용자 클릭 전에 미리 해당 웹사이트를 크롤러가 방문하여 HTML head의 메타 데이터를 크롤링하여 미리보기 화면 생성



#### body 요소

- 브라우저 화면에 나타나는 정보로 실제 내용에 해당한다.



#### Semantic Tag (HTML5에서 새로 제공하는 시맨틱 태그)

- 의미의, 의미론적인

- article / aside / details / figcaption / figure / footer / header / main / mark / nav / section / summary / time


#### Non-Semantic Tag

- div / span / a / p /





#### nth-child / nth-of-type 차이

- <el>:nth-child(n) : el 부모의 모든 자식들 중 n번째 자식이 el이라면 선택, el이 아니면 바뀌지 않음
- <el>:nth-of-type(n) : el 부모의 자식들 중 el인 것들 중에서 n번째를 선택



#### TAG 정리

head : 머릿말

meta : data에 대한 정보를 알려줌 (ex. open graph)

title : 문서 제목

body : 본문

p(paragraph) : 단락, 문단, 절

h1~h6 : 제목, 글자 크기

hr : 단락 구분, 문서의 구분선

br : break, 줄바꿈

p : paragraph, 문단을 나타내는 요소, p요소 안에는 인라인 요소만 포함 가능.

div(division) : 문서 영역이나 섹션의 분할

span : inline 요소, 줄바꿈이 안되고, 폭, 높이 적용도 안됨

table : 표, border, width, summary의 속성값이 있음

caption : summary 역할, css에서 안보이게 함, 스크린 리더기에 활용

col : 빈 태그이지만 유일하게 self close가 없다.

thead : 테이블 헤더 행 그룹

tbody : 테이블 내용 행 그룹

tfoot : 테이블 푸터 행 그룹, 화면상에서 아래에 위치

th(table header) : 셀 제목으로 지정하여 강조되게 표시하는 태그

tr(table row) : 테이블 내의 한 행을 정의하는 태그

td(table data) : 각 행에 포함된 셀을 만들 때 사용되는 태그



### display / visibility

#### display : 요소를 어떻게 표시할지 선택

#### visibility : 요소를 보일지 말지 결정



#### inline / block / inline-block

##### inline

- 줄을 바꾸지 않고 다른 요소와 함께 한 행에 위치하려는 성향

- Tag (a, span, strong, img, br, input, select, textarea, button)
- line-height 속성을 통해 조절
- width, height, margin-top, margin-bottom 속성이 적용되지 않음. (line 안에 있으니까 제멋대로 크기 못바꿈)

##### block

- 한 줄에 나열되지 않고 그 자체로 한 줄을 완전히 차지(기본적으로 width: 100% 속성을 가지고 있음)
- Tag (p, div, h1~h6, ol, li, hr, table, form)
- margin, width, height 속성이 적용됨. (한 줄을 차지하고 있어서 자유자재로 크기 조정 가능)

##### inline-block

- inline과 같이 한 줄에 표현하면서도 margin, width, height 속성을 표현할 수 있음

- margin과 line-height 두가지 속성이 모두 적용됨. (line 안에 있지만 block의 속성을 가져 크기를 조절할 수 있다.)



###### 주의 : inline 속성 태그 안에 block 속성 태그를 넣으면 문법 오류가 발생 (Block이 Inline을 포괄하는 더 큰 개념이기 때문)

ex)

- `<span><p>`문장입니다.`<p><span>` -> 오류
- `<p><span>`문장입니다.`<span><p>`  -> 적절



mt-2 



#### 박스 위치 설정

- relative : 객체가 static일 때의 위치를 기준으로 이동
  - relative 사용하여 이동하게 되면 static일 때의 위치에 잔상이 남아 있음
- absolute : 부모요소 또는 가장 가까이에 있는 조상 요소를 기준으로 이동

## CSS

- Cascading Style Sheets

#### 스타일 적용 우선순위

- inline > 내부참조 > 외부참조



#### em / rem / vh / vw / vmin / vmax

- em : 상위 요소의 크기를 기준으로
- rem : 문서의 최상위 요소(html)의 크기를 기준으로

- vh : 뷰포트의 높이값 * 1/100
- vw : 뷰포트의 너비값 * 1/100
- vimn : 뷰포트의 너비값, 높이값 중 작은 값 * 1/100
- vmax : 뷰포트의 너비값, 높이값 중 큰 값 * 1/100



#### 선택자 우선순위

- ex) p > li {

  }					 에서 `{` 앞 부분이 선택자

- !important(0순위) > inline 스타일 > ID선택자(#) > 클래스 선택자(.class1) > 태그 선택자(<p>) > 전체 선택자(*)
- 인접 형제(+) vs 일반 형제(~)
  - 인접 형제 : 형제 중 첫번째 동생 요소가 조건을 충족시킬 때에만 스타일을 적용
  - 일반 형제 : 조건을 충족하는 모든 동생 요소에 스타일을 적용



#### span tag 사용이유??

- css를 적용시키기 위해서 마크업을 해야하는데 선택자가 없을 때 사용



#### css 적용

- 일반 태그 : p {} // h3 {} // div {}
- 클래스 태그 : .red {} // .blue {}
- 인접 선택자 : .red + .blue + div {}
- 자식 선택자 : ol > li {}
- chocolate ID를 가진 부모 ol의 자식 li : ol#chocolate > li {}
- 자손 선택자 : ul li {}
  - 공백으로 구분하면 자신 아래에 있는 모든 자손에 영향을 줌



## CDN

- Content Delivery Network



### 프레임워크

- 어떠한 목적을 달성하기 위해 복잡하게 얽혀있는 문제를 해결하기 위한 구조

- 클래스와 라이브러리가 합쳐진 형태
- 재사용 가능한 수많은 클래스, 라이브러리들을 융합한 채로 제공
- 종류
  - Django, Bootstrap, Node.js, Spring, ...
  - Bootstrap : HTML, CSS, JS 프레임워크

### 라이브러리

- 소프트웨어 개발 시 사용되는 프로그램의 구성요소
- 공통으로 사용될 수 있는 특정한 기능들을 모듈화한 것



### API

- Application Programming Interface
- 



```html
<form action="#">
    ID: <input type="text"><br>
    PWD: <input type="password">
    <input type="submit" value="로그인"
</form>
```

