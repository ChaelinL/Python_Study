
#기본 예제
#1
pwd = input('비밀번호를 입력하세요 >>> ')
ch_count = 0
num_count = 0

for ch in pwd:
    if ch.isalpha():
        ch_count+=1
    elif ch.isnumeric():
        num_count+=1

if ch_count > 0 and num_count > 0:
    print('가능한 비밀번호입니다.')
else:
    print('불가능한 비밀번호입니다.')

#2
dan = int(input('출력할 구구단을 입력하세요 >>> '))
for n in range(1,10):
    print(f'{dan}X{n}={dan*n}')

#3
eng_dict = {'sun':'태양', 'moon':'달', 'star':'별', 'space':'우주'}
for word in eng_dict:
    print(f'{word}의 뜻: {eng_dict[word]}')


#응용 예제 (p.129)
#1
for n in range(5):
    print(5-n)

#2
n = int(input('임의의 양수를 입력하세요 >>> '))
sum = 0

for i in range(1,n+1):
    sum += i
print(f'1부터 {n}사이 모든 정수의 합계는 {sum}입니다.')

#3
a = int(input('몇 개의 과일을 보관할까요? >>> '))
basket = []

for i in range(a):
    basket.append(input(f'{i+1}번째 과일을 입력하세요 >>> '))

print(f'입력받은 과일들은 {basket}입니다.')

#4
exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]
score = [100 if i+5>100 else i+5 for i in exam]

print(score)

#5
for i in range(1, 100):
    one = i%10
    ten = i//10

    c1 = one%3==0 and one!=0
    c2 = ten%3==0 and ten!=0

    if c1 and c2:
        print('짝짝', end='\t')
    elif c1 or c2:
        print('짝', end='\t')
    else:
        print(i, end='\t')

    if i%10 == 0:
        print()
