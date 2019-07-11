# 딕셔너리 반복문 활용하기

lunch = {
    '중국집': '021-123-5455',
    '분식집': '032-123-2222',
    '일식집': '011-332-2333'
}

# 기본 활용
for key in lunch:
    print(key)
    print(lunch[key])

# .items()
for key, value in lunch.items():
    print(key,value)

# value만 가져오기 .values()
for value in lunch.values():
    print(value)

# key만 가져오기 .keys()
for key in lunch.keys():
    print(key)