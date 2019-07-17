1. 

- 변경할 수 있는 것(mutable) : List, Set, Dictionary
- 변경할 수 없는 것(immutable) : String, Tuple, Set



2. 

```python
odd_list = []
num_list= list(range(1, 51))

for i in range(50):
        odd_list = odd_list + num_list[2*i:2*i+1]

print(odd_list)

# a = list(range(1,51))
# b = a[0::2]  # ':2' : 2개 단위로 자르기
# print(b)
```



3. 

```python
student_dict = {
    '이병주': 18
    'ㅁㄴㅇㄹ': 29
}
```

