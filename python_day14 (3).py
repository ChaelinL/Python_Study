
# 기본 예제 (p.267)
class Computer:
    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print(f'CPU = {self.cpu}')
        print(f'RAM = {self.ram}')
        print(f'VGA = {self.vga}')
        print(f'SSD = {self.ssd}')

desktop = Computer()
desktop.set_spec('i7','16GB','GTX1060','512GB')
desktop.hardware_info()

notebook = Computer()
notebook.set_spec('i5','8GB','MX300','256GB')
notebook.hardware_info()


# 기본 예제 (p.269)
class Calculator:
    def __init__(self):
        self.expr = None

    def input_expr(self):
        expr = input('수식을 입력하세요 >>> ')
        self.expr = expr

    def calculate(self):
        if not self.expr:
            print('input_expr 메소드를 먼저 실행하세요.')
            return
        return eval(self.expr)

calc = Calculator()
calc.input_expr()
print(calc.calculate())


# 응용 예제 (p.270)
# 1
class Book:
    def set_info(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f'책 제목: {self.title}')
        print(f'책 저자: {self.author}')

book1 = Book()
book2 = Book()
book1.set_info('파이썬','민경태')
book2.set_info('어린왕자','생텍쥐페리')

book_list = [book1, book2]
for i in book_list:
    i.print_info()

# 2
class Watch:
    def __init__(self, time):
        self.hour, self.minute, self.second = map(int, time.split(':'))

    def add_hour(self,n):
        self.hour += n
        if self.hour > 23:
            self.hour -= 24

    def add_minute(self,n):
        self.minute += n
        while self.minute > 59:
            self.minute -= 60
            self.add_hour(1)

    def add_second(self,n):
        self.second += n
        while self.second > 59:
            self.second -= 60
            self.add_minute(1)

watch = Watch(input('시간을 입력하세요 >>> '))
watch.add_hour(int(input('계산할 시간을 입력하세요 >>> ')))
watch.add_minute(int(input('계산할 분을 입력하세요 >>> ')))
watch.add_second(int(input('계산할 초를 입력하세요 >>> ')))

print(f'계산된 시간은 {watch.hour}시 {watch.minute}분 {watch.second}초입니다.')


# 3
class Song:
    def set_song(self,title,category):
        self.title = title
        self.category = category
    def print_song(self):
        print(f'{self.title}({self.category})')

class Singer:
    def set_singer(self,name):
        self.name = name

    def hit_song(self,song):
        self.song = song

    def print_singer(self):
        print(f'가수이름: {self.name}')
        print(f'노래제목: ', end='')
        self.song.print_song()

song = Song()
song.set_song('취중진담','발라드')
singer = Singer()
singer.set_singer('김동률')
singer.hit_song(song)
singer.print_singer()