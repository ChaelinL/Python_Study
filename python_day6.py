
#지난 시간 복습

#삼항 연산자
n = int(input('숫자를 입력하세요 >>> '))
print('10보다 큽니다.') if n>10 else print('10보다 작거나 같습니다.')

#문자열 입력을 숫자형으로 전환
map(실행시킬 명령, 반복가능 객체)
n1, n2 = map(int, input('숫자를 두 개 입력하세요. >>> ').split())
print(n1, n2)

# 조건문
# 사용자가 입력한 값이 10 이상일 경우 '10 이상 입니다.' 출력
n = int(input('숫자를 입력하세요 >>> '))
if n>10:
    print('10보다 큽니다.')
elif n==10:
    print('10 입니다.')
else:
    print('10보다 작습니다.')

print('프로그램을 종료합니다.')

#응용 예제 복습 (p.99)
#3
a = int(input('정수1 입력 >>> '))
b = int(input('정수2 입력 >>> '))
c = int(input('정수3 입력 >>> '))

a, b, c = map(int, input('정수를 3개 입력하세요 >>> ').split())

if a>b>c or a>c>b:
    print(f'가장 큰 수는 {a}입니다.')
elif b>a>c or b>c>a:
    print(f'가장 큰 수는 {b}입니다.')
elif c>a>b or c>b>a:
    print(f'가장 큰 수는 {c}입니다.')
else:
    print('모두 같은 값입니다.')

#4
n = input('차량번호를 입력하세요 >>> ')
if int(n[-1])%2==0:
    print(f"차량번호 '{n}'는 오늘 운행가능입니다.")
else:
    print(f"차량번호 '{n}'는 오늘 운행불가입니다.")


#반복문
#n을 입력하여 해당 수만큼 반복하는 반복문을 작성
n = int(input('숫자입력 : '))
while n>0:
    print('반복')
    n-=1

#방법 1
list = []
n = int(input('정수를 입력하세요(종료는 0입니다) >>> '))

while n!=0:
    list.append(n)
    n = int(input('정수를 입력하세요(종료는 0입니다) >>> '))
print(list)

#방법 2
list = []

while True:
    n = int(input('정수를 입력하세요(종료는 0입니다) >>> '))
    if not n:
        break
    list.append(n)
print(list)


#응용 예제 복습 (p.111)
#2
n = 1
while n<=100:
    if n%7==0:
        print(n)
    n+=1

#5
n = 1
while n<=100:
    print(n) if n%10==0  else print(n, end='\t')
    n+=1

#6
n = 1
while n<=9:
    dan = 2
    while dan <=9:
        print(f'{dan}X{n}={dan*n}', end='\t')
        dan+=1
    n+=1
    print()


#for문
#range(n) -> 0~(n-1)까지 범위
#range(n, s) -> n~(s-1)까지 범위
#range(n, s, k) -> n~(s-1)까지 범위, k씩 증가
#역순(k<0)일 경우 -> n~(s+1)까지 범위

for i in range(10, 100, 10):
    print(i)

for _ in range(5):
    print('hello')

dic = {'나비':'butterfly', '꽃':'flower', '벌':'bee'}
for 벌 in dic:
    print(dic[벌])

#i가 짝수일때 0~99만큼 0 반복
list = [0 for i in range(100) if i%2==0]
print(list)


#응용 예제 (p.129)
#1
for i in range(5):
    print(5-i)

#2
a = int(input('임의의 양수를 입력하세요 >>> '))
sum = 0

for i in range(1, a+1):
    sum+=i
print(f'1부터 {a}사이 모든 정수의 합계는 {sum}입니다.')

#4
#방법 1
exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]
score = []

for i in exam:
    score.append(100 if i+5>100 else i+5)
print(score)

#방법 2
exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]
score = [100 if i+5>100 else i+5 for i in exam]
print(score)