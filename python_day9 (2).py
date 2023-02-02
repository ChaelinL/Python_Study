
#기본 예제 (p. 173)
#1
while True:
    p = input('하이픈을 포함하여 전체 주민등록번호를 입력하세요 >>> ')
    if p.find('-')!=6:
        print('하이픈의 위치가 잘못되었습니다.')
        continue
    birthday = p.split('-')[0]
    print(f'생년월일은 {birthday}입니다.')
    break

#2
a_list = ['above', 'cookie', 'app', 'admin', 'bisket', 'apple', 'april']
for i, item in enumerate(a_list):
    if item.find('a')==-1:
        print(f'{a_list.pop(i)} 제거됩니다.')

print(a_list)


# 정규 표현식(Regex) 적용 예시
email = input("이메일을 입력하세요 >>> ")

p = '^[0-9a-zA-Z]+@[a-z]+\.[a-z]+$'

import re
r = re.compile(p)

if r.match(email):
    print("이메일입니다.")
else:
    print("이메일이 아닙니다.")


#응용 예제 (p. 180)
#1
number = input("전화번호를 입력하세요 >>> ")
p = '^\d{2,3}-\d{3,4}-\d{4}$'

import re
r = re.compile(p)

if r.match(number):
    print(number.split('-')[1])

else:
    print("잘못된 전화번호입니다.")

#2
number = input('사업자등록번호를 입력하세요(예: 123-45-67890) >>> ')
p = '^\d{3}-\d{2}-\d{5}$'

import re
r = re.compile(p)

if r.match(number):
    print("올바른 형식입니다.")
else:
    print("올바른 형식이 아닙니다.")

#3
info = '"김철수",85'

name = info.split(',')[0].strip('"')
score = info.split(',')[1].strip()

print(f"이름은 {name}이고, 점수는 {score}점입니다.")