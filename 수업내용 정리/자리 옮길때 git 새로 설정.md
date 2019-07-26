# 자리 옮길때 git 새로 설정

###  과정

#### 1. 시작 -> 자격증명 -> git 관련 모두 제거

#### 2. Git Bash 설정

- git bash

1. cd ~ 상태에서 git config --global user.name byeongjulee222
2. git config --global user.email dave.juya777@gmail.com
3. git config --global --list로 확인



##### cf) git init으로 (master표시) 된거 지우는 방법

- rm -rf .git



- ##### 알고리즘에 사용할 3.5.3 버전으로 설정

1. python -V 로 버전 확인
2. mkdir ~/python-virtualenv 로 폴더 만들기
3. python -m venv ~/python-virtualenv/3.7.3 로 폴더 만들기

4. 알고리즘에 사용할 3.5 버전을 기본으로 설정



code ~/.bashrc

```python
export FLASK_ENV=development
alias jp="jupyter notebook"
alias venv="source ~/python-virtualenv/3.7.3/Scripts/activate"
```

입력 후 저장



cd ~ 에서

venv 입력 후 버전확인



시작 - 시스템 환경 변수 편집 - 환경 변수 -  PATH 더블 클릭 - `~Python37` 두개를 밑으로(4번째, 5번째)

끌때는 deactivate

---

- ##### 버전 변경 과정

  - 3.7.3으로 할 때 venv
    - deactivate를 하지 않더라도 git bash를 종료하면 3.5.3으로 돌아간다.
  - 3.5.3으로 할 때 deactivate
  - 항상  python -V로 버전 확인