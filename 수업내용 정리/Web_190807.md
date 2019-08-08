[TOC]

# 

### 2. relative (상대위치)

- 과거(static)일 때의 위치 기준으로 이동



### 3. absolute (절대위치)

- 가장 가까이 있는 조상요소(static 제외)를 기준으로 이동.



### 4. fixed (고정위치)

- 부모 요소와 관계없이 브라우저의 viewport를 기준으로 좌표 프로퍼티를 사용하여 이동





## Bootstrap

- twiter



#### CDN (Content Delevery Network)

- 컨텐츠를 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템



##### 기본 세팅

```python
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

</head>

<body>


  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
    integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
  </script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
  </script>
</body>

</html>
```



##### CSS History

1. 레이아웃이 없던 시절
2. 테이블 레이아웃
3. 프레임 레이아웃
4. CSS(float / position)
5. flex box()
6. grid system (2차원 배열)
   - grid가 flex box 상위 버전이긴 하지만 완전히 대체하는 것은 아니다.





```python
.container>.row>.square.col-1{$}*12
```

