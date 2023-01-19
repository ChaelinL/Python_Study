
#기본 예제
#1
name = "Kai"
print("내 이름은 %s입니다."%name)
print(f"내 이름은 {name}입니다.")

#2
name = input("이름을 입력하세요 >>> ")
print(f"입력된 이름은 {name}입니다.")

#3
price = 50000
n = int(input("할부 개월 입력 >>> "))
print(f"매달 내는 돈은 {price/n}원 입니다.")


#응용 예제 p66
#1
a = float(input("첫 번째 실수를 입력하세요 >>> "))
b = float(input("두 번째 실수를 입력하세요 >>> "))
print(f"{a}와 {b}의 합은 {a+b}입니다.")

#2
a = int(input("1~12월 사이의 월을 입력하세요 >>> "))
list = [31, 28, 31, 30, 31, 30, 31, 31, 30 ,31, 30, 31]
print(f"{a}월은 {list[a-1]}까지 있습니다.")

#3
english_dict = {'flower':'꽃','fly':'날다','floor':'바닥'}
a = input("영어 단어를 입력하세요 >>> ")
print(f"{a}: {english_dict[a]}")

#4
a = input("희망하는 수학여행지를 입력하세요 >>> ")
b = input("희망하는 수학여행지를 입력하세요 >>> ")
c = input("희망하는 수학여행지를 입력하세요 >>> ")
set = {a, b, c}

print(f"조사된 수학여행지는 {set}입니다.")
