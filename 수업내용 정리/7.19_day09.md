## 1번.

* 
* 파일명 기준 잘 지키기



최근 50주간 데이터 중에 주간 박스오피스 TOP10데이터를 수집합니다

-->  targetDt 50번 돌리기

3. 다양성 영화/상업 영화를 모두 포함하여야 합니다. -->multiMovieYn default가 둘 다 포함(--> 안써도됨)

4. 5.  도 default가 모두 포함이라 안써도됨





 단계적 접근

50주 -> 1주 (for문 없이) -> 3주 -----> 50주 : 처음부터 50주로 돌리면 3000번의 키 요청 횟수 오버할 수 있다.



주의사항 

- 구글링 가능
- 상의 가능
- 남의 코드 작성 X
- 코드 가독성에 유의





키 : ac0a219e5d10b44fc8a54fb33e6c4d3a



pprint 사용하기

from datetime import datetime, timedelta

datetime(2019, 7, 13) - datetime()

targerDt.strftime('%Y%m%d')     # import 불필요





timedelta(weeks=i)

- i 이전의 시각을 구함

- for  range(50)



1. 데이터 불러오기

   1.1 key, url, targetDt 준비

   1.2 요청보내서 json 데이터 받기

   1.3 위에서 받은 데이터로 원하는 데이터 리스트로 가져오기

   1.4 필드 준비/ 딕셔너리 만들기







##  2번

1. dictreader
2. 요청보내서 딕셔너리 만들고
3. dictwriter





----

1. 어떤 프로젝트인지 1~2줄 요약
2. 01.py에 대한 설명
   - 어떤 데이터를 가져와서 어떻게 저장했는지
   - 과정이나 시행착오

(각 문제마다 작성할 것!!!)



다하고 내 깃헙에 pjt_01에 레포지토리 푸시