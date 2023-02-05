
# 파일객체 = open(파일명, 모드)

# w - 파일이 없으면 만듦 (쓰기)
# r - 파일이 없으면 에러 (읽기)
# a - 파일이 없으면 만듦 (추가=읽기+쓰기)

# 파일명만 적을 시, 상대경로 적용

# with as (resource) : 이 블록이 끝났을 때 해당 리소스를 close 해준다.

# ~~~.bin -> binary (2진 파일)
# ~~~.txt -> +t

with open('test.txt', 'w', encoding='UTF-8') as f:
    f.write('hello\n')
    f.write('안녕하세요')


# 기본 예제 (p. 232)
import time

file = time.strftime('%Y-%m-%d') + '.txt'
with open('file','a',encoding='UTF-8') as f:
    while True:
        schedule = input('오늘의 스케줄을 입력하세요 >>> ')
        # 아무것도 입력하지 않고 엔터를 누른 경우 종료
        # True - False 이외의 값
        # False - 비어있거나 없다는 것을 의미하는 모든 것 (0, [], (), "" 등)
        if not schedule:
            break
        f.write(schedule+'\n')


# 스케쥴 메뉴 만들기 (예제 연장선)
import time

file_name = time.strftime('%Y-%m-%d')+'.txt'

def add_schedule(schedule):
    if not schedule:
        print("할 일을 입력하지 않았습니다.")
        return
    with open(file_name,'a',encoding='UTF-8') as f:
        f.write(schedule+'\n')
    print('할 일이 추가되었습니다.')


def print_schedule():
    with open(file_name, 'r', encoding='UTF-8') as f:
        # 방법 1: readlines() - 파일 안의 내용을 전부 list로 들고옴
        for s in f.readlines():
            print(s.rstrip('\n'))

        # 방법 2: readline() - 파일 안의 내용을 str으로 들고옴
        while True:
            line = f.readline()
            if not line:
                break
            print(s.rstrip('\n'))


    # 다른 파일에서 import schedule 실행
    # import schedule
    #
    # while True:
    #     print('=' * 20)
    #     print('1. 할 일 추가')
    #     print('2. 할 일 확인')
    #     print('=' * 20)
    #     select = int(input('선택하세요 >>> '))
    #
    #     if select == 1:
    #         schedule.add_schedule(input('할 일 입력 >>> '))
    #     elif select == 2:
    #         schedule.print_schedule()


# 응용 예제 (p.238)
#1
def a():
    nation = ['그리스', '아테네', '독일', '베를린', '러시아', '모스크바', '미국', '워싱턴']
    with open('nation.txt', 'w', encoding='UTF-8') as f:
        for i in range(0, len(nation), 2):
            f.write(nation[i]+'-'+nation[i+1]+'\n')
a()

#2
def x():
    list=[]
    with open('연락처.txt', 'r') as f:
        for i in f.readlines():
            list.append(i)

    with open('연락처.txt', 'w') as f:
        for i in list:
            if i.find('011'):
                f.write(i)
            else:
                i = i.lstrip('011')
                f.write('010'+i)
x()
