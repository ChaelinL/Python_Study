
#기본 예제
#1
a, b = 10 ,20
print(f"a = {a}, b = {b}")
a, b = b, a
print(f"a = {a}, b = {b}")

#2
a = 15
print(f"{a}>10 : {a>10}")
print(f"{a}<10 : {a<10}")
print(f"{a}>=10 : {a>=10}")
print(f"{a}<=10 : {a<=10}")
print(f"{a}==10 : {a==10}")
print(f"{a}!=10 : {a!=10}")

a = 10
b = 0
print(f"not {a} : {not a}")
print(f"not {b} : {not b}")
print(f"{a} > 0 and {b} > 0 : {a>0 and b>0}")
print(f"{a} > 0 or {b} > 0 : {a>0 or b>0}")

#3
tree = "#"
space = " "
print(space*4 + tree*1)
print(space*3 + tree*3)
print(space*2 + tree*5)
print(space*1 + tree*7)
print(space*0 + tree*9)

a = 10
b = 20
result = (a-b) if (a>=b) else (b-a)
print(f"{a}과 {b}의 차이는 {result}입니다.")


#응용 예제 p85
#1
a = int(input("10 ~ 99 사이의 정수를 입력하세요 >>> "))
ten = a//10
one = a%10
print(f"십의 자리: {ten}\n 일의 자리: {one}")

#2
a = int(input("초를 입력하세요 >>> "))
hour = a//3600
min = a//60 - (hour*60)
sec = a%60
print(f"변환 결과는 {hour}시간 {min}분 {sec}초입니다.")

#3
a = int(input("4자리 사원번호를 입력하세요 >>> "))
b = "오전" if a%10>=5 else "오후"

print(f"근무 시간은 {b}입니다.")

#4
a = int(input("한 박스에 20개의 라면을 담을 수 있습니다.\n라면의 개수를 입력하시면 필요한 박스 수를 알려드립니다.\n라면의 개수를 입력하세요 >>> "))
b = a//20+1 if a%20!=0 else a//20

print(f"{a}개 라면을 담으려면 {b}박스가 필요합니다.")

#5
a = int(input("국어 점수를 입력하세요 >>> "))
b = int(input("영어 점수를 입력하세요 >>> "))
c = int(input("수학 점수를 입력하세요 >>> "))
avg = (a+b+c)/3
result = "합격" if avg>=80 else "불합격"

print(f"평균은 {avg}점이고, 결과는 {result}입니다.")