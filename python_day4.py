
#기본 예제
#1
age = int(input('몇 살입니까? >>> '))
if age >=20:
    print('성인')
else:
    print('미성년자')

#2
age = int(input('몇 살입니까? >>> '))
if age <= 7:
    print('미취학')
elif age <= 13:
    print('초등학생')
elif age <= 16:
    print('중학생')
elif age <= 19:
    print('고등학생')
else:
    print('성인')


#응용 예제
#1
score = int(input('점수를 입력하세요 >>> '))
if score>=90:
    print(f'점수는 {score}점이고, 학점은 A학점입니다.')
elif score>=80:
    print(f'점수는 {score}점이고, 학점은 B학점입니다.')
elif score>=70:
    print(f'점수는 {score}점이고, 학점은 C학점입니다.')
elif score>=60:
    print(f'점수는 {score}점이고, 학점은 D학점입니다.')
else:
    print(f'점수는 {score}점이고, 학점은 F학점입니다.')

#2
num = int(input('정수를 입력하세요 >>> '))
if num%3==0:
    print(f'{num}은 3의 배수입니다.')
else:
   print(f'{num}은 3의 배수가 아닙니다.')

#3
a = int(input('정수1 입력 >>> '))
b = int(input('정수2 입력 >>> '))
c = int(input('정수3 입력 >>> '))

if a>b>c or a>c>b:
    print(f'가장 큰 수는 {a}입니다.')
elif b>a>c or b>c>a:
    print(f'가장 큰 수는 {b}입니다.')
else:
    print(f'가장 큰 수는 {c}입니다.')

#4
num = input('차량번호를 입력하세요 >>> ')
if int(num[-1:])%2==0:
    print(f"차량번호 '{num}'는 오늘 운행가능입니다.")
else:
    print(f"차량번호 '{num}'는 오늘 운행불가입니다.")
