# 협업할 때, Master/Branch를 통한 git 사용 방법



## 새 작업 공간 만들기

1. New organization

2. $0 으로 선택 (github pro 계정이면 사용 가능)

3. Choose Team for Open Source

4. 프로젝트 이름 입력하고, 협업하는 사람 계정 추가

5. Master 공간에서 fork 뜨고 내 github에서 repository 추가됐는지 확인

6. fork 떠 온 내 repository에서 주소 복사해서 git clone

7. `git remote add upstream + (master 주소)`

   ---> bash에서 `git remote -v` 찍고 주소 확인 (4개 떠야함)



## Branch 떠 온 곳에서 변경사항 push

### 작업은 항상 branch에서 할 것



#### 1. branch 만들기 + branch로 이동 한 번에 

--->`git checkout -b` + (사용할 branch 이름)

1. 만약 이름 설정 잘못해서 다시 하려면

   ---> `git checkout master`로 master 위치로 이동 후

   --->`git branch -d + (branch 이름)`으로 삭제



#### 2. 작업 완료 후 커밋하려면

---> branch 위치에서 `git add` --> `git commit` --> `git push origin + (branch 이름)`

---> github 들어가서 **pull request 보내기**



#### 3. 마스터가 승인했으면

1. `git checkout master`로 위치 이동
2. `git pull upstream master`로 마스터의 최종본 받아오기
3. `git log --oneline --graph`로 연결 상태 확인