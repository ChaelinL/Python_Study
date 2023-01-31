
#사용자 함수
#TypeHint
def add(x:int, y:int) -> str:
    print(x+y)
    return 'abc'

print(add(1, 2))


#매개변수가 몇 개인지(넘어오는 인자가 몇 개인지) 모르는 경우
#가변인자(variable arguments) -> args
def add(*args: int) -> int:
    return(sum(args))

print(add(5, 10, 15, 20))

#키워드 가변인자(keyword variable arguments) -> kwargs
#가변인자와 함께 쓸 때 무조건 뒤에 와야한다.

def add(**kwargs: int) -> int:
    total = 0
    for i in kwargs:
        total += kwargs[i]
    return total

print(add(a=5, b=10, c=15, d=20))