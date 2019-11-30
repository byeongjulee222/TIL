## IaaS

- Infrastructure as a Service
- 공급 업체를 통해 사용자가 서버, 스토리지 및 너트워킹과 같은 컴퓨팅 리소스를 이용할 수 있는 클라우드 서비스.
- 사용자는 서비스 제공업체의 인프라 내에서 자체 플랫폼과 어플리케이션을 사용한다.
- ex) AWS - EC2 
  - 장점 : 가상의 컴퓨터 한 대를 빌려서 그 환경을 처음부터 세팅할 수 있어 원하는 기능을 제약없이 구현할 수 있다
  - 단점 : 배포를 위해 모든 작업을 스스로 해야하며, 그 과정에서 많은 시행착오가 발생할 수 있다. 온전히 개발에만 집중하는 것이 아니라, 배포를 위한 부가적인 코스트가 소모된다.



## PaaS

- Platform as a Service
- 사용자가 어플리케이션을 개발, 관리 및 제공할 수 있는 클라우드 환경을 제공하는 클라우드 서비스
- 사용자는 사전에 구축된 tool 세트를 사용하여 자체 어플리케이션을 개발, 커스터마이즈, 테스트 할 수 있다.
- ex) HEROKU / AWS - EB(Elastic Beanstalk)
  - 장점 : OS, 네트워크, 데이터베이스 등 배포를 위한 환경 설정이 되어있어, web app 만 업로드 해도 쉽고 빠르게 배포가 된다. 상대적으로 heroku가 eb보다 비교적 빠르고 쉽게 배포되는 편이다.
  - 단점 : 이미 환경이 갖추어져 있는 서버에 배포만 하는 특성상 제한된 기능만을 수행할 수 있다.





project 폴더에 settings 폴더 생성

settings 폴더로 settings.py 옮기고 이름을 base.py로 변경

`__init__.py` , `local.py` , `product.py` 생성

local.py, product.py에 

```python
from .base import *

SECRET_KEY = '9j==%5s2v$6j4(+3j&r&i48d(pg^1)6&v)=_5zkmsus2y!*$(_'

DEBUG = True

ALLOWED_HOSTS = []
```

복붙

- product.py에서는 DEBUG = False



- pip install python-decouple
- 최상위 폴더에 .env 파일 만들고 SECRET_KEY='' (공백 없도록) 작성



local.py, product.py에

```python
from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY', default='임의의 50글자 입력')

DEBUG = True

ALLOWED_HOSTS = []
```

- 임의의 50글자 : https://miniwebtool.com/django-secret-key-generator/



- runserver해서 잘 작동하는지 확인





