import random

#기본 예제 (p. 208)

def secure_name(name):
    return name[0]+"**"

def secure_no(no):
    return no[0:8]+"******"

def secure_phone(phone):
    return phone.replace(phone[4:8], '****')

# ==> 다른 파일에서 함수 import 불러오기
# from python_day11 (3) import *
#
# print(secure_name('김철수'))
# print(secure_no('000817-3412344'))
# print(secure_phone('010-2839-0839'))


#기본 예제 (p.213)
import random

dice = random.randint(1,6)
while True:
    user = int(input("주사위 값은 얼마일까요? >>> "))
    if dice == user:
        print(f"{dice}! 정답입니다.")
        break
    else:
        print("오답입니다. 다시 시도하세요.")


#기본 예제 (p. 218)
from datetime import *

start = datetime.now()
total = 0
for num in range(1, 10000001):
    total+=num
end = datetime.now()

elapse = end - start
elapse = elapse.total_seconds()

print(f"총 합은 {total}입니다.")
print(f"총 {elapse}초가 소요되었습니다.")

#time 추가 예제
import time

while True:
    print(time.strftime('\r%Y년 %m월 %d일 %H시 %M분 %S초'), end='')
    time.sleep(1)


#응용 예제 (p.221)
#1
pot = [i for i in range(1,46)]
jackpot = []

for i in range(6):
    random.shuffle(pot)
    x = pot.pop()
    print(f"{i+1}번째 당첨번호는 {x}입니다.")
    jackpot.append(x)
    time.sleep(2)

jackpot.sort()
print(f"이번 당첨번호는 {jackpot}입니다.")


#2
import math

ran = random.randint(1, 100)
start = time.time()

print("UpDown게임을 시작합니다.")
while True:
    user = int(input('어떤 값일까요? >>> '))
    if ran == user:
        print("정답입니다.")
        break
    if ran > user:
        print("Up")
    else:
        print("Down")
end = time.time()

elapse = end-start
print(f"{math.floor(elapse)}초 만에 성공했습니다.")
