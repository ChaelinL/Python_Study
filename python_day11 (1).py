import time

# sleep(s) -> time 모듈의 함수로써 s초 만큼 기다린다

a = 0
while True:
    print(a, end=f'\r{a}')
    a+=1
    time.sleep(1)


# time -> 현재 시간을 반환
# ctime(n) -> n(시간)을 형식에 맞춰 반환
print(time.ctime(time.time()))

# srtftime('') -> 문자열 형식의 시간 포맷에 맞춰 현재 시간을 반환
while True:
    print(time.strftime('\r%Y년 %m월 %d일 %H시 %M분 %S초'), end='')
    time.sleep(1)