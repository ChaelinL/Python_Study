
#사용자 함수 예제 (p. 188~)

#인수가 있는 함수
#1
def introduce(name, age):
    print(f"내 이름은 {name}이고, 나이는 {age}살입니다.")

introduce('James', 18)

#2
def add(x:int,y:int):
    print(x+y)
    return 'abc'

print(add(1,2))


#가변 매개변수
#1
def show(*args):
    for item in args:
        print(item)

show('happy')
show('happy', 'birthday')

#2
def add(*args: int):
    return(sum(args))

print(add(1, 2, 3, 4, 5))


#키워드 가변인자
def add(**kwargs: int):
    total = 0
    for i in kwargs:
        total += kwargs[i]
    return total

print(add(a=1, b=2, c=3, d=4, e=5))


#디폴트 매개변수
#1
def greet(message='안녕하세요'):
    print(message)

greet('반갑습니다')
greet()

#2
def greet(name, message='안녕하세요'):
    print(f"{name}님 {message}.")

greet('김철수')


#기본 예제 (p. 191)
def add(*args):
    print(f"{args}의 합은 {sum(args)}입니다.")

add(1,2)
add(1,2,3,4)


#반환값이 있는 함수
def address():
    str = '우편번호 12345\n'
    str += '서울시 영등포구 여의도동'
    return str
print(address())

#다중 반환
def calculator(*args):
    return sum(args), sum(args)/len(args), max(args), min(args)

#방법 1
a, b, c, d = calculator(1, 2, 3, 4, 5)
print('합계', a)
print('평균', b)
print('최댓값', c)
print('최솟값', d)

#방법 2
result = calculator(1, 2, 3, 4, 5)
print('합계', result[0])
print('평균', result[1])
print('최댓값', result[2])
print('최솟값', result[3])


#기본 예제 (p. 195)
def coffee_machine(money, pick):
    print(f"{money}원에 {pick}를 선택하셨습니다.")
    menu = {
        '아메리카노':1000,
        '카페라떼':1500,
        '카푸치노':2000
    }

    if pick not in menu:
        print(f"{pick}는 판매하지 않습니다.")
        return money, '없는 메뉴'
    elif menu[pick]>money:
        print(f"{pick}는 {money}원입니다.")
        return money, '금액 부족'
    else:
        return money - menu[pick], pick

order = input("커피를 선택하세요. (아메리카노, 카페라떼, 카푸치노) >>> ")
pay = int(input("얼마를 내시나요? >>> "))

change, coffee = coffee_machine(pay, order)
print(f"잔돈{change}원, 커피 {coffee}")


#전역변수, 지역변수
a = 15

def add(x,y):
    global a #이거 안쓰면 결과값은 8, 2가 아닌 8, 15가 됨.
    a = 2
    print(x+y)

add(3, 5)
print(a)


#응용 예제 (p. 199)
#1
def vending_machine(money):
    price = 700
    count = money // 700
    change = 0
    for i in range(count+1):
        change = money - (i)*price
        print(f"음료수={i}개, 잔돈={change}원")

vending_machine(3000)

#2
def get_average(marks):
    total = 0
    for i in marks:
        total += marks[i]
    return total/len(marks)

marks = {
        '국어': 90,
        '영어': 80,
        '수학': 85,
}
average = get_average(marks)
print(f"평균은 {average}점입니다.")

#3
total = 0
def gift(dic, who, money):
    global total
    total += money
    dic[who] = money

wedding = {}
gift(wedding, '영희', 5)
gift(wedding, '철수', 3)
gift(wedding, '이모', 10)
print(f"축의금 명단: {wedding}")
print(f"전체 축의금: {total}")