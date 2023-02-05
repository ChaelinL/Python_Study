
# 파스칼 케이스 (각 단어의 첫 글자는 무조건 대문자) --> class에 적용됨
#   첫 글자를 무조건 대문자로 시작한다.
#   이어지는 단어의 첫 글자 또한 대문자로 시작한다.
#   student number -> StudentNumber

# 카멜 케이스 ( 첫 다넝의 글자만 소문자, 나머지는 파스칼 케이스와 같음) --> 함수, 메서드, 변수에 적용됨
#   student number -> studentNumber

# 스네이크 케이스 (모든 단어는 대문자면 대문자로 통일, 소문자면 소문자로 통일. 단, 이어지는 단어가 있는 경우 _ 로 구분)
#   student number -> student_number
#   student number -> STUDENT_NUMBER


class student:
    # 클래스의 생성자 -> 클래스가 생성될 때 자동으로 실행되는 메소드
    #               -> 클래스의 생성조건을 만들어 줄 수 있다.
    def __init__(self, num, name, address, phone):
        # self -> 객체 자기 자신을 가르키는 변수
        #      -> 객체 안에서 만드는 모든 메소드에 self는 첫번째 매개변수로 등장
        self.num = num
        self.name = name
        self.address = address
        self.phone = phone

    # 메소드는 동사로 시작한다는 암묵적 약속 존재
    def print_info(self):
        print(f'[{self.name}]')
        print(f'학번: {self.num}')
        print(f'주소: {self.address}')
        print(f'번호: {self.phone}')

list = []

with open('info.csv','r') as f:
    f.readline()
    for i in f.readlines():
        sub = i.rstrip('\n').split(',')
        st = student(int(sub[0]), sub[1], sub[2], sub[3])
        list.append(st)

list[0].print_info()


# 기본 예제 (p. 269)
class Calculator:
    def __init__(self):
        self.expr = None

    def input_expr(self):
        self.expr = input('수식을 입력하세요 >>> ')

    def calculate(self):
        if not self.expr:
            print('input_expr 메소드를 먼저 실행하세요.')
            return
        return eval(self.expr)

calc = Calculator()
calc.input_expr()
print(calc.calculate())


# 응용 예제 (p. 270)
#1
class Book:
    def set_info(self, name, author):
        self.name = name
        self.author = author

    def print_info(self):
        print(f'책 제목 : {self.name}')
        print(f'책 저자 : {self.author}')

book1 = Book()
book2 = Book()
book1.set_info('파이썬','민경태')
book2.set_info('어린왕자','생택쥐페리')

book_list = [book1, book2]

for book in book_list:
    book.print_info()