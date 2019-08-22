[TOC]

# Django

#### 기본 설정

시작 전에 파이썬 버전 변경(최상위 환경 // 알고리즘 수업할 때는 반대로)

![image](https://user-images.githubusercontent.com/52685247/62986257-a7f7d980-be75-11e9-9dc3-cf71bc2737d9.png)

3.7버전이 3.5버전 위에 위치하도록

### 1. Django (동적)

#### 1.1 특징

- 의존성 
  - 본인의 컴퓨터에서 잘 작동하던 프로그램도, 다른 프로그램에 설치했을 때 잘 동작하리라는 보장이 없음.
  - 파이썬도 같은 버전, 같은 모듈을 쓴다는 보장이 없다.
  - 따라서, 특정 프로그램만을 실행하기 위한 파이썬 환경을 따로 만들고, 그 환경 속에서만 모듈 관리 및 앱을 실행시키기 위해 가상환경을 설정한다.
  - 다른 앱을 실행시키는 일이 생기면 그 가상환경을 빠져나와 다른 환경을 만드는 방식으로 진행한다.

#### 1.2 가상환경 실행

- 윈도우에서는 작업전에 가상환경을 실행시켜야 한다.
  - 시스템이 종료되면 가상환경도 실행이 종료된다.

1. python -m venv (가상환경 경로+이름)

   ex) python -m venv ssafy

2. source venv/Scripts/activate

3. 끌 때는 deactivate



- 가상환경 맞는지 확인 : pip list



- 가상환경 선택 
  - 00_django_intro 폴더에서 open VSCode
  - Python : Select interpreter -> 3.7.3 venv 선택 -> 좌하단에 python 3.7.3 (venv) 확인



---

#### terminal 단축키 설정

`code ~/.bashrc`

alias venv="source ~/python-virtualenv/3.7.3/Scripts/activate"에서 사용했던 단축 명령어와는 다른 venv



Preferences :  Open settings (JSON)

`"terminal.integrated.cwd": "${workspaceFolder}",` 추가

(새로 업데이트 하면서 변경되었기 때문에 새로 설정)



Keyboard Shortcuts -> integrate 검색 -> Integrated Terminal 단축키 `ctrl+~`로 설정

---



- pip install django



- django-admin startproject django_intro .



- python manage.py startapp pages



- settings.py에서 

- ​    'pages',

  ​    'pages.apps.PagesConfig',



- 서버 키는 방법
  - python manage.py runserver (manage.py가 있는 폴더내에서)





### 2. django 기본 구조

M : Model
T : Template

V : View

- 요청 + 반응 과정

![image](https://user-images.githubusercontent.com/52685247/62988461-78e66580-be7f-11e9-93f6-c379e8697d9e.png)

`__init__.py` : 초기화해주는 파일 (만질 일 없음)

`urls.py` : url과 웹간의 연결 관리

 : 사용자의 요청을 가장 먼저 받는 곳

![image](https://user-images.githubusercontent.com/52685247/62988495-9ca9ab80-be7f-11e9-8135-9d6adda54d75.png)

#### 2.1 앱 만들기

- python manage.py startapp (앱 이름) --> 폴더가 새로 만들어짐
  - 앱의 이름은 -s와 같이 복수형으로 만든다. (ex.pages)

- 안에 view.py, model.py 가 있을 것이다. (우리가 수정할 부분)





#### 2.2 앱 등록하기

- settings.py -> INSTALLED_APPS
  - 이미 적혀있는 목록은 기본 내장 app
- 가장 위에 'pages.apps.PagesConfig', 추가 (폴더, 파일을 타고 들어가는 과정)
  - 끝에 `,` 붙이는거 잊지말기. 한 줄을 작성하더라도 붙이기.





#### 2.3 코드 작성 순서 !!!

1. views : 만들고자하는 view 함수 작성
2. urls : views에서 만든 함수에 주소를 연결
3. templates : 해당 view 함수가 호출될 때, 보여질 페이지



##### pages.Views.py

```python
def index(request): # 첫번째 인자는 반드시 request
    return render(request, 'index.html') # render()의 첫번째 인자도 반드시 request
```



##### django_intro/urls.py (요청을 가장 먼저 받아들이는 곳)

- path('index/', views.index),
  - 사용자가 `/index`로 들어오면 views.py 안에 있는 index 함수를 사용할 것이다.

```python
from django.contrib import admin
from django.urls import path
from pages import views # 생성한 app pages 폴더 안의 views.py 파일

urlpatterns = [
    path('index/', views.index), # url 경로 마지막에 '/'를 붙이는 습관
    path('admin/', admin.site.urls),
]
```



##### pages 안에 templates 폴더 만들고 index.html 파일 만든다.





##### 실습

view 함수 이름은 introduce

introduce.html을 보여준다.



##### variable routing

#####  동적 라우팅

- 주소 자체를 동적으로 변경



#### 실습

1. 자기소개

   introduce 확장 이름과 나이를 받아서 출력

2. 숫자 2개를 받아 두 수의 곱셈 결과를 출력(times)

3. 반지름 값을 받아 원의 넓이 출력(area)



##### Django Template Language(DTL)

- django template에서 사용하는 내장 template system이다.
- 조건, 반복, 변수 치환, 필터 등 많은 기능을 제공한다.





#### form 이용하여 데이터 주고받기

views.py에서 함수 정의 (단순히 데이터를 주는 것만 정의)

```python
def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message') # THROW에서 넘겨준 메세지를 message라는 변수에 담는다. (request라는 요청 안에서 데이터가 넘어오기 때문)
    
    return render(request, 'catch.html')
```





##### urls.py

```python
    path('throw/', views.throw),
```





##### throw.html

```html
<form action="" method="GET">
  <label for="message">THROW</label>
  <input type="text" id="message" name="message"> # 라벨을 누르더라도 검색창을 선택하도록 (id를 통해 연결)
  <input type="submit"> # 데이터 전송 버튼 생성
</form>
```

input태그 안에 id="" 은 나중에 JS 할 때 사용

submit을 누르는 순간 action="" 으로 데이터를 전송

 ---> 





---

### artii로 데이터 주고받기

```python
def art(request):
    return render(request, 'art.html')


def result(request):
    # 1. art에서 form으로 보낸 데이터를 받는다.
    word = request.GET.get('word')

    # 2. ARTII API의 font list로 요청을 보내 응답을 text로 받는다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    # .text: 응답을 text 형태로 바꾼다. (사용하지 않으면 response [200])
    # print(fonts)
    # 3. str을 list로 바꾼다. (랜덤으로 돌려서 폰트를 변경하기 위해)
    fonts = fonts.split('\n')

    # 4. fonts list 안에 들어있는 요소 중 하나를 선택해서 변수에 저장
    font = random.choice(fonts)

    # 5. 위에서 만든 word와 font를 가지고 다시 요청을 보내 응답 결과를 받는다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {'response': response,}
    return render(request, 'result.html', context)
```



```html
<h1>ASCII ART에 오신것을 환영합니다. ^____________^</h1>

<pre>{{ response }}</pre> # 출력해주는 방식 그대로 보여주기 위해 pre태그 사용
```





---

### post 방식으로 데이터 전송하기





---

#### csrf 사이트간 요청 위조

- 웹 어플리케이션 취약점 중 하나로, 사용자가 자신의 의도와 무관하게 공격자가 의도한 행동을 해서 특정 웹 페이지의 보안을 무력화 시키거나, 수정, 삭제 등의 강제적인 작업을 하도록 하는 공격 방법

- django는 최소한의 안전장치를 위해 자신이 부여한 랜덤 hash값을 token으로 부여한다. 이 token값이 없는 요청은 잘못된 요청이라고 판단하여 접근을 거부한다.(403 error)





##### views.py

```python
def user_new(request):
    return render(request, 'user_new.html')


def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {'name': name, 'pwd': pwd,}
    return render(request, 'user_create.html', context)
```







##### urls.py

```python
    path('user_create/', views.user_create),  # 뒤에 '/' 붙여야됨
    path('user_new/', views.user_new),
```







##### url에 암호가 노출되지 않도록



settings.py

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', # 이 부분에서 인증이 되지 않아 걸리게 됨.
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```





user_new.html

```html
  {% csrf_token %} # 값을 추가해주어 현재 ID와 PW를 입력하는 사용자가 인증된 사람인 것을 알려줌 (django에서 정해준 명령어. 맞춰주어야 함.)
```





![image](https://user-images.githubusercontent.com/52685247/63139840-b3d0d080-c01a-11e9-9e5d-4e4753188880.png)

- hash값이 계속 변함





---

## 정적 파일 (Static)

- image / css / js 파일과 같이 해당 내용이 고정되어 응답을 할 때 별도의 처리없이 그대로 보여주면 되는 파일들







## CRUD

Create Read Update Delete



#### ORM

- sql <---> python 사이에서 번역해주는 역할

- 장점

  - sql을 몰라도 db 사용이 가능하다.
  - sql의 절차적인 접근이 아닌 객체 지향적 접근 가능
  - 매핑 정보가 명확하여 ERD를 보는 것에 대한 의존도를 낮출 수 있다.
  - ORM은 독립적으로 작성되어 있고, 해당 객체들을 재활용할 수 있다. 개발자는 객체에 집중함으로써, 해당 DB에 종속될 필요없이 자유롭게 개발할 수 있다.

- 단점

  - ORM만으로 거대한 서비스를 완전히 구현하기가 어렵다.

    -> 사용하기는 편하지만, 설계는 매우 신중하게 해야함.

    -> 프로젝트의 규모가 커질 경우 난이도가 올라가게 된다.

    -> 순수 SQL보다 약간의 속도 저하가 생길 수 있다.

  - 이미 프로세스가 많은 시스템에서는 ORM으로 대체하기가 어렵다.

- 단점이 있음에도 사용하는 이유?

  - 생산성!!!
  - ORM을 사용하여 얻게되는 생산성은 약간의 성능저하나 다른 단점들을 상쇄할 만큼 뛰어나기 때문
  - 장점으로 인한 생산성 증가가 훨씬 크기 때문에 현대에는 대부분의 프레임워크들이 ORM을 사용하고 있다.
  - 즉, 우리는 DB를 객체(object) - 인스턴스(instance)로 조작하기 위해 ORM을 배운다.



#### 게시판 만들기 실습

```python
# 게시판 만들기 실습
class Article(models.Model):    # models.Model의 상속을 받는다.(github으로 확인함.)
    # id(프라이머리 키)는 기본적으로 처음 테이블 생성시 자동드로 만들어진다.
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10) # 클래스 변수(DB의 필드)
    content = models.TextField() # 클래스 변수(DB의 필드)
    created_at = models.DateTimeField(auto_now_add=True) # 클래스 변수(DB의 필드)
    updated_at = models.DateTimeField(auto_now=True) # 수정될 때마다 변경
```



- 모델의 개념

  - 모델은 단일한 데이터에 대한 정보를 가지고 있다.

  - 필수적인 필드(컬럼, column)와 데이터(레코드, row)에 대한 정보를 포함한다. 일반적으로 각각의 **모델(클래스)**는 단일한 데이터베이스 **테이블과 매핑(연결, 연동)**된다.

  - 모델은 부가적인 메타데이터를 가진 **DB의 구조(layout)**를 의미

  - 사용자가 저장하는 데이터들의 필수적인 필드와 동작(behavior)을 포함

    --> 동작? `(primary_key=True)`와 같이 괄호 안에 입력하여 수행하는 일



#### 필드 종류

(django 공식 사이트 설명 : https://docs.djangoproject.com/en/2.2/ref/models/fields/)

- CharField()
  - 길이의 제한이 있는 문자열을 넣을 때 사용
  - **`max_length`는 필수 인자다**.
  - 필드의 최대 길이(문자)이며 DB 와 django의 유효성검사(값을 검증)에서 사용됨.
  - 텍스트의 양이 많을 경우 `TextField()`로 사용
- TextField()
  - 글의 수가 많을 때 사용
  - max_length 옵션을 줄 수 있지만, 모델과 실제 DB에는 적용되지 않음. 길이 제한을 주고싶다면 CharField()를 사용해야 한다.

- DateTimeField()
  - 시간과 날짜를 기록하기 위한 필드
  - `auto_now_add=True`
    - django ORM이 **최초 INSERT(테이블에 데이터 입력)시에만** 현재 날짜와 시간을  작성
    - **최초 생성일자**가 들어감
  - `auto_now=True`
    - django ORM이 **SAVE를 할 때마다** 현재 날짜와 시간을 작성
    - **최종 수정일자**가 들어감



#### Model의 로직

- DB 컴럼과 어떠한 타입으로 정의할 것인지에 대해 `django.db` 모듈의 `models`의 상속을 받아서 적용된다. `from django.db import models` 으로 기본적으로 입력되어 있음(프레임워크에서 기본적으로 입력해둠.)
- 각 모델은 **`django.db.models.Model` 클래스의 서브 클래스**로 표현된다.(자식 클래스)

- 모든 필드는 **기본적으로 NOT NULL 조건**이 붙는다. (NULL 값이 들어갈 수 없다.)
- 각각의 **클래스 변수**들은 **모델의 데이터베이스 필드**를 나타낸다.



#### Migrations

- 작업 2가지

1. migrations

   ```bash
   $ python manage.py makemigrations
   ```

   - makemigrations 명령어는 모델(model.py)을 작성/변경한 사항을 django에게 알리는 작업. (ORM에 보낼 PYTHON 코드 설계도를 작성)

   - 모델(models.py)을 작성/변경한 사항을 django에게 알리는 작업
   - 테이블에 대한 설계도를 생성 (파일이 만들어짐, django ORM이 만들어줌.)

2. migrate

   - migrations로 만든 설계도를 기반으로 실제 `db.sqlite3`를 DB 테이블에 반영한다.
   - **모델에서의 변경사항들과 DB 스키마가 동기화**를 이룬다.



##### 추가사항

```bash
$ python manage.py sqlmigrate app_name 0001
```

- migration 하고나서
- 해당 migrations 설계도가 SQL문으로 어떻게 해석되어서 동작할지 미리 볼 수 있다.



```bash
$ python manage.py showmigrations
```

- migrations 설계도가 migrate 됐는지 안됐는지 확인

  `[X]` : 추가됐다는 표시
  
  `[ ]` : 아직 추가 안됐다는 표시



- 과정 확인 명령어 (해석본)
  - python manage.py sqlmigrate articles 0001



##### 수정 후에는 업데이트

- python manage.py makemigrations



#### SQLite 설치

- db.sqlite3 확인하기 위해
- 설정 -> SQLite Open Database -> db.sqlite3 선택



#### Migrate

- python manage.py migrate

```
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, articles, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying articles.0001_initial... OK
  Applying articles.0002_article_updated_at... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
  ---> INSTALLED APPS에 기본적으로 있던 django app들이 migrate 됨.
```



---

### :warning: Model 변경 시 작성 순서

1. `Models.py` : 작성 및 변경(생성/ 수정)
2. `makemigrations` : migration 파일 만들기 (설계도 생성)
3. `migrate` : 실제 DB에 적용 및 동기화 (테이블 생성)

---

테이블의 이름은 app 이름과 model에 작성한 class 이름이 조합되어져서 자동으로 만들어진다 (**모두 소문자**)

모델의 클래스 변수들은 반드시 **소문자**로 작성한다.





```bash
sqlite> .tables
articles_article            auth_user_user_permissions
auth_group                  django_admin_log
auth_group_permissions      django_content_type
auth_permission             django_migrations
auth_user                   django_session
auth_user_groups
sqlite> .schema articles_article
CREATE TABLE IF NOT EXISTS "articles_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "tT, "title" varchar(10) NOCREATE TABLE IF NOT EXISTS "articles_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULitle" varchar(10) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL, "updated_at"
L, "content" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
```



CRUD (DB API 조작)

1. Django Shell
   - django 프로젝트 설정이 로딩된 파이썬 shell
   - 일반 파이썬 shell로는 django 환경에 접근 불가
   - 즉, django 프로젝트 환경에서 파이썬 shell을 활용한다고 생각



### CREATE

- QuerySet 기본개념
  - 전달받은 객체의 목록
    - QuerySet : 쿼리 set 객체
    - Query : 단일 객체
  - DB로부터 데이터를 읽고, 필터를 걸거나 정렬 등을 수행
  - Query를 던지는 Language(django ORM)를 활용해서 DB에게 데이터에 대한 조작을 요구한다
  - objects 사용하여 **다수의 데이터를 가져오는 함수를 사용할 때 반환되는 객체**
  - 단일한 객체를 반환(return)할 때는 테이블(class)의 인스턴스로 리턴됨



- objects
  - Model Manager와 Django Model 사이의 Query 연산의 인터페이스 역할을 해주는 친구
  - 즉, `models.py`에 설정한 테이블(class)을 불러와서 사용할 때 DB와의 인터페이스 역할(Query를 날려주는)을 하는 매니저이다.
  - 쉽게 이해하려면 ORM의 역할이라고 생각하면 된다.
  - **DB <------------objects-------------> Python Class(models.py)**
  - Manager(objects)를 통해 특정 데이터를 조작(메서드)할 수 있다.



- 테이블 내용을 전부 조회(READ)
- DB에 쿼리를 날려서 인스턴스 객체 전부를 달라고 하는 뜻
- 만약 레코드가 하나라면, 인스턴스 단일 객체로 반환 (ex. id와 같이 하나 있는 값)
- 두 개 이상이면, QuerySet 형태로 반환

`Article.objects.all()`(python code) --> `SELECT * FROM articles_article` (DB에 입력되는 방식)

---

##### 데이터 객체를 만드는(생성, CREATE)하는 3가지 방법

1. 첫 번째 방식

   ```bash
   $ python manage.py shell
   
   # SQL문으로 작성했다면? - 특정 테이블에 새로운 레코드(행)을 추가하여 데이터 추가
   # INSERT INTO table (column1, column2, ...) VALUES (value1, value2, ...)
   # INSERT INTO articles_article (title, content) VALUES ('first', 'django!')
   
   # ORM을 활용하여 Python에서 작성한다면
   >>> article = Article() # 인스턴스 객체 생성 (OOP에서 했던 방식)
   >>> article.title = 'first' # 인스턴스 변수(title)에 값을 할당
   >>> article.content = 'django!' # 인스턴스 변수(content)에 값을 할당
   
   # save를 하지 않으면 아직 DB에 값이 저장되지 않음
   >>> article
   <Article: Article object (None)>
   >>> Article.objects.all()
   <QeurySet []>
   
   # save를 하고 확인해보면 저장된 것을 확인할 수 있다.
   >>> article.save()
   >>> article
   <Article: Article object (1)>
   >>> Article.objects.all()
   <QuerySet [<Article: Article object (1)>]>
   
   # 인스턴스 article을 활용하여 변수에 접근할 수 있다(저장된 값 확인)
   >>> article.title
   'first'
   >>> article.content
   'django!'
   >>> article.created_at
   datetime.datetime(2019, 8, 21, 2, 43, 54, 572816, tzinfo=<UTC>)
   >>> articles.updated_at
   datetime.datetime(2019, 8, 21, 2, 43, 54, 572816, tzinfo=<UTC>)
   ```

   

2. 두 번째 방식

   ```bash
   >>> article = Article(title='second', content='django!!')
   >>> article.save()
   ```





3. 세 번째 방식

   - `create()`를 사용하면 QuerySet 객체를 생성하고 저장하는 로직이 한 번의 스텝으로 끝난다.
   - save 하기 전, 유효성 검사를 할 수 가 없어서 잘 사용하지 않는다.

   ```bash
   >>> Article.objects.create(title='third', content='django!!!')
   <Article: Article object (3)>
   
   # return 값이 있기 때문에 변수에 담을 수 있다.
   >>> test = Article.objects.all()
   >>> test
   <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
   ```

   

##### 유효성 검사

- save 전에 `.full_clean()` 메서드를 통해 article이라는 인스턴스 객체가 검증(validation)에 적합한지를 알아볼 수 있다.
- `models.py`에 필드 속성과 옵션에 따라 검증을 진행한다.

---

### READ

```python
# 1. SELECT * FROM articles_article;
# 1. DB에 있는 모든 글 가져오기
>>>Article.objects.all()

---------------------------------------------

# 2. SELECT * FROM articles_article WHERE title='first';  # ';' 붙여야한다.
# 2. DB에 저장된 글 중에서 title이 first인 글만 가져오기
>>> Article.objects.filter(title='first')

--------------------------------------------------

# 3. SELECT * FROM articles_article WHERE title='first' LIMIT 1;
# 3. DB에 저장된 글 중에서 title이 first인 글 중에서 첫번째 글만 가져오기
>>> Article.objects.filter(title='first').first()
>>> Article.objects.filter(title='first').last() # 마지막 값

------------------------------------------------

# 4-1. SELECT * FROM articles_article WHERE id=1;
# 4-1. DB에 저장된 글 중에서 PK가ㅓ 1인 글만 가져오기
>>> Article.objects.get(pk=1)

# PK만 .get()으로 가져올 수 있다. (.get()은 값이 중복이거나 일치하는 값이 없으면 에러를 발생시킨다.) 즉, pk에만 사용하자.

# 4-2. filter의 경우, 존재하지 않으면 에러가 아닌 빈 QuerySet을 반환한다. 마치 딕셔너리에서 value를 꺼낼 때 [] 방식으로 꺼내냐, .get()으로 꺼내냐 하는 차이와 유사하다.
>>> Article.objects.filert(pk=100)
<QuerySet []>

# 4-3. filter / get
# filter 자체가 여러 값을 가져올 수 있기 때문에 django가 개수를 보장하지 못한다. 그래서 0개, 1개라도 무조건 QuerySet으로 반환한다.

--------------------------------------------------------

# 5-1. 오름차순
# SELECT * FROM articles_article ORDER BY title ASC;
>>> Article.objects.order_by('pk')

# 5-2. 내림차순
# SELECT * FROM articles_article ORDER BY title DESC;
>>> Article.objects.order_by('-pk')

------------------------------------------------------------

# 6. QuerySet은 리스트 자료형은 아니지만, 리스트에서 할 수 있는 인덱스 접근 및 슬라이싱이 모두 가능하다.
>>> Article.objects.all()[2]
>>> Article.objects.all()[1:2]

------------------------------------------------------------

# 7. LIKE / startswith / endswith
# django ORM은 이름(title)과 필터(contains)를 더블언더스코어(__)로 구분한다.
# 더블언더스코어 == 던더(dunder)스코어

# LIKE
>>> Article.objects.filter(title__contains ='fir')

# startswith
>>> Article.objects.filter(title__startswith ='fir')

# endswith
>>> Article.objects.filter(title__endswith ='!')
```









- models.py에서 추가

```python
    def __str__(self):
        return f'{self.pk}번 글 - {self.title} : {self.content}'
```

- exit로 shell을 빠져나간 후 다시 진행
- python manage.py shell
- from articles.models import Article
- Article.objects.all() 로 확인



```bash
>>> Article.objects.create(title='first', content='django!!!!!!')
<Article: 6번 글 - first : django!!!!!!>

>>> Article.objects.filter(title='first')
<QuerySet [<Article: 1번 글 - first : django!>, <Article: 6번 글 - first : django!!!!!!>]>
```







.filter로 가져왔을 때는 QuerySet과 같이 리스트로 출력

.get으로 가져왔을 때는 <> 자체로 출력

---

### UPDATE

```python
# article 인스턴스 객체의 인스턴스 변수에 들어있는 기존 값을 변경하고 저장
>>> article = Article.objects.get(pk=1)

>>> article.title = 'byebye'

>>> article.save()
```



### DELETE

```python
# article 인스턴스 객체를 생성 후 .delete() 메서드를 호출
>>> article = Article.objects.get(pk=1)

>>> article.delete()
```

- pk = 1 인 값을 지우면 pk=2 부터 데이터가 시작
- 새로 데이터를 추가하더라도 pk=1이 추가되는 것이 아니라, 마지막 pk 번호 다음 순서로 생성됨



#### 정리

- 핵심은 우리는 ORM을 통해 클래스의 인스턴스 객체로 DB를 조작할 수 있다는 것!
- 앞으로 CRUD 로직을 직접 작성하면서 위에서 배운 코드들을 다시 활용하게 될 것이다.





### ADMIN

- 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지.
- `models.py`에 작성한 클래스를 `admin.py`에 등록하고 관리.
- record 생성 여부 확인에 매우 유용하고, 직접 레코드를 작성할 수도 있다.
- CRUD 로직을 모두 관리자 페이지에서 사용할 수 있다.





- admin.py

```python
from django.contrib import admin
from .models import Article # '.' : 명시적 상대경로 표현

# Register your models here.
class AriticleAdmin(admin.ModelAdmin):
    # 튜플이나 리스트로 작성 (대부분 튜플로 작성)
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
    # 리스트에 필터 추가
    list_filter = ('created_at',) # 하나의 튜플 만들 때 뒤에 ',' 붙여줘야 함.
    # 항목에 링크 걸기
    list_display_links = ('content',)
    # 링크 안에 들어가지 않고 바로 수정할 수 있게
    list_editable = ('title',)
    # 한 페이지에 보이는 개수 조절 (기본값:100)
    list_per_page = 2

admin.site.register(Article, AriticleAdmin)
```



### 관리자 변경 목록(change list) 커스터마이징

https://docs.djangoproject.com/ko/2.2/ref/models/fields/

1. list_display
   - admin 페이지에서 우리가 `models.py`에 정의한 각각의 속성(컬럼)들의 값(레코드)을 보여준다.
2. list_filter
   - 특정 필드에 의해 변경 목록을 필터링 할 수 있게 해주는 filter 사이드 바를 추가한다.
   - 표시되는 필터의 유형은 필드의 유형에 따라 다르다
3. list_display_links
   - 목록 내에서 링크로 지정할 필드 적용(설정하지 않으면 기본값을 첫번째 필드에 링크가 적용)
4. list_editable
   - 목록 상에서 직접 수정할 필드 적용
5. list_per_page
   - 한 페이지에 표시되는 항목 수를 제어(기본 값: 100)



---

### Django extensions

- Django-extension은 커스텀 확장 tool이다.
- Django app 구조로 되어있기 때문에 프로젝트에서 사용하기 위해서는 app 등록 과정을 거쳐야 한다.





##### * %hist --> 지금까지 shell에 입력했던 명령어 목록 출력

















#### GET -> POST 바꾼 이유?

1.  사용자는 django에게 **HTML 파일을 줘!(GET)**가 아니라 **~한 레코드(글)을 생성해줘(POST)** 이기 때문에 GET보다는 POST 요청이 더 적절하다.
2. 데이터는 URL에 노출되면 안된다.(우리가 URL에 접근하는 방식은 모두 GET) query의 형태를 통해 DB schema를 유추할 수 있게 되고, 이는 보안 측면에서 매우 취약하게 된다.
3. 모델(DB)를 조작하는 친구는 GET이 아닌 POST 요청! 왜냐? DB를 수정하는 것은 매우 중요한 일이고, 그에 따른 **최소한의 신원확인**이 필요하다!!! (GET으로 동작하게된다면 악성사용자가 URL만으로 글을 작성, 수정, 삭제할 수 있게 된다.)



#### Redirect

- POST 요청은 HTML 문서를 render 하는게 아니라, `~좀 처리해줘(요청)`의 의미이기 때문에 요청을 처리하고 나서의 결과를 보기 위한 페이지로 넘겨줘야 한다.



#### POST 요청으로 변경 후 변화하는 것

- form을 통해 전송한 데이터를 받을 때도 `request.POST`로 받아야 한다.
- 글이 작성되면 실제로 URL에 데이터가 나타나지 않게 된다.
- html 문서를 요청하는 게 아니기 때문에 html 문서를 받아볼 수 있는 다른 페이지로 redirect하게 된다.















