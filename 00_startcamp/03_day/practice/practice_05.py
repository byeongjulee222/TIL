'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''
# 문자열 => 리스트로 형변환을 하는게 포인트!!!

#----1----#
# prices = input('물품 가격을 입력하세요: ')

# prices_list = prices.split(';')             # 목록의 값들을 ';'을 기준으로 나눔
#                                             # 실행 결과 : 리스트로 바뀜
# prices_list.sort(reverse=True)              # 목록의 배열을 내림차순으로
#                                             # sort 사용할 때 문자형을 숫자형으로 변경해야
#                                             # 크기별로 정렬이 가능하다

# for i in prices_list:                       
#     print(int(i))                     # 결과값이 세로로 출력


#----2----#
# prices = input('물품 가격을 입력하세요: ')

# prices_list = prices.split(';')

# prices_list.sort(reverse = True)

# print(prices_list)                  # 결과값이 리스트 형식으로 가로로 출력

#----3----#
# 빈 리스트를 먼저 만들어두고 풀이
prices = input('물품 가격을 입력하세요: ')
makes = prices.split(';')

boxes = []
for make in makes:
    boxes.append(int(make))
boxes.sort(reverse=True)

for box in boxes:
    print(box)


# append() : 리스트에 요소를 추가
# list.append(1) : 리스트에 1을 추가한다.