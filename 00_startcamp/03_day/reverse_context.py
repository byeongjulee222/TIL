# DOCstring : 주석과 같은 효과
"""
이 함수는 블라블라
누가 만들었고
어떻게 사용하고
이런 함수입니다.
"""

"""
다음과 같은 내용의 파일 quest.txt 가 있다.
0
1
2
3

이 파일의 내용을 다음과 같이 역순으로 reverse_quest.txt 라는 파일로 저장하시오.
3
2
1
0

"""

# 1. 읽고
# 2. 뒤집고
# 3. 작성하기

#----1번째----#
with open('quest.txt', 'r') as f:
    all_text = f.readlines()
    
all_text.reverse()    # or all_text[::-1]

with open('reverse_quest.txt', 'w') as f: 
    f.writelines(all_text)                  # or for line in all_text:
                                            #        f.write(line)


#----2번째----#
# with open('quest.txt', 'r') as f:
#     all_text = f.read()

# with open('reverse_quest.txt', 'w') as f:
#     f.writelines(f'{all_text[::-1].strip()}\n')

#----3번째----#
# with open('quest.txt','r') as rf, open('reverse_quest.txt','w') as wf:
#     for line in reversed(rf.readlines()):
#         wf.write(line)