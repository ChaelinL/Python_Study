
#기본 예제
#1
n = 10
while n>=1:
    print(n)
    n-=1

#2
my_list = []

n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))

while n!=0:
    my_list.append(n)
    n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))

print(my_list)

#3
day = 1
while day<=5:
    hour=1
    while hour<=3:
        print(f'{day}일차 {hour}교시입니다')
        hour+=1
    day+=1

#4
dan = 2
while dan<=9:
    n=1
    while n<=9:
        print(f'{dan}X{n}={dan*n}')
        n+=1
    dan+=1


#응용 예제
#1
a = int(input('정수를 입력하세요 >>> '))
n = 1
while n<=a:
    print(f'{n}번째 Hello')
    n+=1

if a<=0:
    print('잘못된 입력입니다.')

#2
n = 1
while n<=100:
    if n%7==0:
        print(n)
    n+=1

#3
money = int(input('자판기에 얼마를 넣을까요? >>> '))
coffee = 0

while money>=300:
    coffee+=1
    money-=300
    print(f'커피 {coffee}잔, 잔돈 {money}원')

#4
numset = set()

while len(numset)<5:
    n = int(input('0 ~ 9 사이 정수를 입력하세요 >>> '))
    numset.add(n)

print('모두 입력되었습니다.')
print(f'입력된 값은 {numset}입니다.')

#5
n = 1
while n<=100:
    if n%10==0:
        print(n)
    else:
        print(n, end="\t")
    n+=1

#6
dan = 2
while dan<=9:
    num=1
    while num<=9:
        print(f'{dan}X{num}={dan*num}', end="\t")
        num+=1
    print()
    dan+=1