
# random 모듈

import random

# 업다운 게임
# 랜덤으로 컴퓨터가 1 ~ 100 사이의 숫자를 뽑습니다.
# 사용자는 총 5번 입력을 시도 (정수)

def up_down():
    ran = random.randint(1,100)
    for i in range (5):
        print(f"{i+1}번째 시도입니다.")
        num = int(input("1부터 100 사이의 숫자를 입력하세요 >>> "))
        if num == ran:
            print("정답입니다.")
            break

        if i == 4:
            print(f"정답은 {ran}입니다.")
            break

        if num > ran:
            print("down")
        else:
            print("up")


# time 모듈
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


# 로또 추첨 프로그램

# random 모듈
# shuffle(반복가능객체) - 해당 객체를 무작위로 섞어줌

# time 모듈
# sleep(s) - s초만큼 기다림

# list.sort() - 해당 리스트를 오름차순으로 정렬

import random
import time

def lotto():
    pot = [i for i in range(1, 46)]
    jackpot = []

    for i in range(6):
        random.shuffle(pot)
        x = pot.pop(len(pot)-1)
        print(f"{i + 1}번째 당첨번호는 {x}입니다.")
        jackpot.append(x)
        time.sleep(2)

    jackpot.sort()
    print(jackpot)

print(lotto())