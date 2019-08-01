[TOC]

# CSS_190801

- CSS (Cascading Style Sheet)
  - Cascading : 쏟아지는
  - HTML의 마크업 언어. 웹사이트에 표현되는 방법을 정해주는 언어



- 프로퍼티 값의 단위

  1. 키워드
  2. 크기단위
  3. 색깔

  



#### Style Guide

1. 들여쓰기 2문자
2. 클래스, 아이디명은 케밥 케이스(kebob-case)를 사용 : 가운데에 '-' 으로 연결
3. 다중 선택 시, 한 줄에 선택자를 하나씩 작성

```css
.bold,
.yellow,
.bold {
  font-weight: bold;
}
```

4. 모든 스타일 뒤에는 ';' 붙여줘야 한다.

5. 스타일 지정 시 아이디,  태그 대신에 클래스를 사용한다.(되도록, 대부분)

6. 숫자 0 이후에는 불필요한 단위를 작성하지 않는다.

7. 폰트 불러올 때 `@import` 대신 `<link>`  방법을 사용한다. (head 안에 작성)

8. 가능한 단축어(축약형)를 사용한다.

   (단, 불필요하게 남용하는 것은 피한다.)

   

참고 사이트 : https://ui.toast.com/fe-guide/ko_HTMLCSS









- 프로젝트 진행 시, 외부참조 방법을 사용

  - 이유? '컴포넌트화' 해서 적용할 사항이 겹치는 부분을 공통적으로 사용하고,

    다르게 적용할 경우 각각의 파일로 따로 적용하는 것이 편하기 때문.



- 마진상쇄
  - 위 아래 박스의 상하 마진 범위가 겹칠 때, 둘 중 큰 마진 길이로 덮어지는 현상
    - 같은 부모 아래 형제관계일 때 발생

https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Box_Model/Mastering_margin_collapsing

