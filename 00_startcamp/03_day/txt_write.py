# 변수에 만들고 싶은 파일을 open() 해야 한다.
# open() 할 때 r: 읽기 / w: 쓰기(+덮어쓰기) / a: 추가
# f = open('만들 파일 명', '행동')    # 파일 조작할 때 f 사용
# 메모장에 1~10까지 머리번호 입력

#----1----#
f = open('ssafy.txt', 'w')
for i in range(10):
    f.write(f'This is line {i+1}.\n')     # 여기에 글을 쓰겠다 // \n: next line의 약자
f.close()           # 끝나고 무조건 닫아줘야 함

#----2----#
# with 구문 (context manager)
with open('with ssafy.txt', 'w') as f:          # f를 변수로 쓰겠다
     for i in range(10):
         f.write(f'This is line {i+1}.\n')      # 안에 내용이 끝나면 스스로 실행을 멈춤.
                                                # open(~) 명령어보다 with 구문이 더 직관적이고 편하다.

#----3----#
# writelines() : list를 넣어주면, 요소 하나당 한 줄씩 작성
with open('ssafy.txt', 'w') as f:               # w가 덮어쓰기로 작용
    f.writelines(['0.\n', '1.\n', '2.\n', '3'])


# escape 문자
# \n : 개행문자(다음 줄 이동)
# \t : 탭문자
# \\ : 백슬래쉬를 사용하기 위해
# \' : 따옴표 사용
# \" : 쌍따옴표