# read() : 개행문자를 포함한 하나의 문자열
with open('with ssafy.txt', 'r') as f:
    all_text = f.read()                    # 박스(크기)를 지정
    print(all_text)

# readlines() : 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 list로 만들어 냄.
with open('with ssafy.txt', 'r') as f:
    lines = f.readlines()                   # 박스(크기)를 지정
    for line in lines:
        print(line)                         # 두 줄로 나오는 결과 --> 읽어오는 txt에 이미 \n이 있어서.
                                            # print(line.strip()) 입력해주면 \n 없이 출력됨.
        # print(dir(line))                  # dir() : ()안의 함수 뒤에 사용할 수 있는 명령어가 무엇인지 나열