import re

#메소드
#객체가 들고 있는 (함수) -> 메소드 [ex. 파이썬]
#객체가 들고 있지 않은 (함수) -> 함수 [ex. C언어]

#def 이름(매개변수):
#    코드

#함수는 호출에 의해서 실행
#함수 호출 -> 이름(인자)

#전역변수 -> 프로그램이 종료되면 사라짐
a = 15

#매개변수 -> 함수가 종료되면 사라짐
#매개변수를 넣어줬다면 반드시 매개변수를 채우는 인자가 필요
def add(x, y):
    #지역변수 -> 함수가 종료되면 사라짐
    global a #전역변수 a를 사용할 것임을 선언
    a = 2
    print(x+y)

add(3, 5)
print(a)


#str class (객체)
#문자열 메소드 -> str이 들고있는 함수

#왼쪽 :<
#오른쪽 :>
#가운데 :^
# :와 기호(<,>,^) 사이에 문자 넣으면 빈 공간 해당 문자로 채워짐

print("10자리 폭 왼쪽 정렬 {:>10d}".format(123))
print("10자리 폭 왼쪽 정렬 {:^10d}".format(123))
print("10자리 폭 왼쪽 정렬 {:<10d}".format(123))
print("10자리 폭 왼쪽 정렬 {:*>10d}".format(123))
print("10자리 폭 왼쪽 정렬 {:*^10d}".format(123))

#count() 메소드
s = 'hello hi'
print(s.count('h'))

#find() 메소드
s = 'hello hi'
print(s.find('h'))

#split() 메소드
s = '홍길동:13:01029381857'
print(s.split(':')[0])

#replace() 메소드
s = '홍길동:13:01029381857'
print(s.replace(':', '-'))

#strip -> 문자열의 양 끝에 있는 불필요한 문자 제거
#lstrip -> 문자열의 왼쪽 끝에 있는 불필요한 문자 제거
#rstrip -> 문자열의 오른쪽 끝에 있는 불필요한 문자 제거


#기본 예제
#1
while True:
    p = input('하이픈을 포함하여 전체 주민등록번호를 입력하세요 >>> ')
    if p.find('-')!=6:
        print('하이픈의 위치가 잘못되었습니다.')
        continue
    birthday = p.split('-')[0]
    print(f'생년월일은 {birthday}입니다.')
    break


#정규 표현식 regex
p = input('이메일 주소를 입력하세요 : ')

email = '^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z.]+$'
r = re.compile(email)

if r.match(p):
    print('이메일입니다.')
else:
    print('이메일이 아닙니다.')


#리스트 메소드
list = ['cherry', 'apple', 'banana']
item = list.pop()
print(item)
print(list)

#세트 메소드
set1 = {'cherry', 'apple', 'banana'}
set2 = {'cherry', 'apple', 'orange'}

print(set1&set2) #교집합
print(set1|set2) #합집합
print(set1-set2) #차집합


#응용 예제 (p.180)
#1
number = input('번호를 입력하세요 >>> ')
r = re.compile('^\d{2,3}-\d{3,4}-\d{4}$')

if r.match(number):
    print(number.split('-')[1])
else:
    print('전화번호가 아닙니다.')

#2
number = input('사업자등록번호를 입력하세요 >>> ')
r = re.compile('^\d{3}-\d{2}-\d{5}$')

if r.match(number):
     print('올바른 형식입니다.')
else:
     print('올바르지 않은 형식입니다.')

#3
data = '"김철수",85'

name = data.split(',')[0].strip('"')
score = data.split(',')[1].strip()
print(f'이름은 {name}이고, 점수는 {score}입니다.')
