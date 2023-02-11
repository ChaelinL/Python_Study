
# 응용 예제 (p.270)
# 2
class Watch:
    def __init__(self, time: str):
        # 'HH:mm:ss' -> ['HH', 'mm', 'ss']
        # 방법 1
        args = time.split(':')
        self.hour = int(args[0])
        self.minute = int(args[1])
        self.second = int(args[2])

        # 방법 2
        self.hour, self.minute, self.second = map(int, time.split(':'))

    def add_hour(self, n):
        self.hour += n
        if self.hour > 23:
            self.hour -= 24

    def add_minute(self, n):
        self.minute += n
        while self.minute > 59:
            self.minute -= 60
            self.add_hour(1)

    def second(self, n):
        self.second += n
        while self.second > 59:
            self.second -= 60
            self.add_minute(1)

    # or
    def second(self, n):
        self.second += n
        if self.second > 59:
            self.second %= 60
            self.add_minute(self.second // 60)

# import 파일명
#
# watch = python_day14 (1).Watch(input('시간을 입력하세요 >>> '))
#
# watch.add_hour(int(input('계산할 시간을 입력하세요 >>> ')))
# watch.add_minute(int(input('계산할 분을 입력하세요 >>> ')))
# watch.add_second(int(input('계산할 초를 입력하세요 >>> ')))
#
# print(f'계산된 시간은 {watch.hour}시 {watch.minute}분 {watch.second}초입니다.')


# 3
class Song:
    def set_song(self, title, category):
        self.title = title
        self.category = category

    def print_song(self):
        print(f'{self.title}({self.category})')

class Singer:
    def set_singer(self, name):
        self.name = name

    def set_hit_song(self, song):
        self.song = song

    def print_singer(self):
        print(f'가수이름: {self.name}')
        print(f'노래제목:', end ="")
        self.song.print_song()
        
# import 파일명
#
# song = 파일명.Song()
# song.set_song('취중진담', '발라드')
#
# singer = 파일명.Singer()
# singer.set_singer('김동률')
# singer.set_hit_song(song)
#
# singer.print_singer()
