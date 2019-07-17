1. 

```python
n = 5
m = 9

for i in range(m):
        print('*' * n)
        
# for i in range(m):
#	for j in range(n):
#		print('*', end='')
#	print()
```



2. 

```python
student = {'python': 80, 'algorithm': 99, 'django': 89, 'flask': 83}
sum = 0
people = len(student)
for i in student:
        sum += student[i]
print(sum/people)

# sum(student.values()) / len(student)

# sum(student.values()) / len(student.keys())
```



3. 

```python
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

blood_counter = {}

for blood_type in blood_types:
        if blood_type in blood_counter:
                blood_counter[blood_type] += 1
        else:
                blood_counter[blood_type] = 1
print(blood_counter)

##---다른방법---##
# for blood_type in blood_types:
#	blood_counter[blood_type] = blood_types.count(blood_type)
# print(blood_counter)
```

