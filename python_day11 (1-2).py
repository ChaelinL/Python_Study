
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