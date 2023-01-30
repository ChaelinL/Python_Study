
#기본 예제
#1
while True:
    city=input('대한민국의 수도는 어디인가요? >>> ')
    if city=='서울'or'seoul'or'SEOUL':
        print('정답입니다.')
        break
    else:
        print('오답입니다. 다시 시도하세요.')

#2
hobbies = []
while True:
    hobby=input('취미를 입력하세요(종료는 그냥 엔터) >> ')
    if hobby=='':
        print('입력된 취미가 모두 저장되었습니다.')
        break
    else:
        hobbies.append(hobby)

print(hobbies)

#3
fruits = ['사과', '감귤']
count = 3

while count>0:
    fruit = input('어떤 과일을 저장할까요? >>> ')
    if fruit in fruits:
        print('동일한 과일이 있습니다.')
        continue
    fruits.append(fruit)
    count-=1
    print(f'입력이 {count}번 남았습니다.')

print(f'5개의 과일은 {fruits}입니다.')

#4
count = 0
total = 0

while count<5:
    n=int(input(f'{count+1}번째 정수를 입력하세요 >>> '))
    if n<=0:
        print('0 이하의 정수는 처리할 수 없습니다.')
        continue
    count+=1
    total+=n

print(f'입력된 5개 양수의 총 합은 {total}입니다.')


#응용 예제 (p.141)
#1
money = 10000
use = 0

while money>0:
    print(f'현재 {money}원이 있습니다.')
    if money == 0:
        break

    use = int(input('사용할 금액 >>> '))
    if use<=0:
        print('0 이하의 금액은 사용할 수 없습니다.')
    elif use>money:
        print(f'{use-money}원이 부족합니다.')
    else:
        money-=use

print('현재 0원이 있습니다.')

#2
while True:
    star = int(input('이번 영화의 평점을 입력하세요 >>> '))
    if 1<=star<=5:
        print('평점: '+'★'*star)
        break
    print('평점은 1~5 사이만 입력할 수 있습니다.')

#3
answer = "qwerty"
count = 0

while True:
    if count == 5:
        print('비밀번호 입력 횟수를 초과했습니다.')
        break

    password = input('비밀번호를 입력하세요 >>> ')
    if password == answer:
        print('비밀번호를 맞혔습니다.')
        break
    count += 1

#4
for dan in range(3,10):
    if dan%2==0:
        print('')
        continue
    for n in range(1,dan+1):
        print(f'{dan}x{n}={dan*n}')