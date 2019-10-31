from time import sleep

def sleep_3s():
    sleep(3)
    print('Wake up!')

print('Start sleeping')
sleep_3s()
# 코드의 실행을 블락
print('End of program')
