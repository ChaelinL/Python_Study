
# 파일 입출력
# 텍스트 파일 생성하기
with open('myfile.txt','w',encoding='UTF-8') as f:
    f.write('hello\n')
    f.write('안녕하세요')

# 텍스트 파일에 내용 추가하기
with open('myfile.txt','a',encoding='UTF-8') as f:
    f.write('\nHello\n')
    f.write('만나서 반갑습니다.')
    print('hello.txt 파일에 새로운 내용이 추가되었습니다.')


# 기본 예제 (p.232)
import time

with open(time.strftime('%Y-%m-%d')+'.txt','at') as f:
    while True:
        schedule = input('오늘의 스케쥴을 입력하세요 >>> ')
        if not schedule:
            break
        else:
            f.write(schedule+"\n")


# 기본 예제 응용 (스케쥴 메뉴 만들기)
import time

file_name = time.strftime('%Y-%m-%d')+".txt"

def add_schedule(schedule):
    if not schedule:
        print("할 일을 입력하지 않았습니다.")
        return
    with open(file_name,'a') as f:
        f.write(schedule+'\n')
    print("할 일이 추가되었습니다.")

def print_schedule():
    with open(file_name, 'r') as f:
        for s in f.readlines():
            print(s.rstrip('\n'))


# 기본 예제 (p.237)
with open('엄마돼지아기돼지.txt','r') as f:
    line_list = f.readlines()

    count = 0
    for line in line_list:
        for ch in line:
            if ch == "꿀":
                count+=1

    print(f'꿀은 전체 {count}번 나타납니다.')


# 응용 예제 (p.238)
# 1
with open('nation.txt','w') as f:
    nation = ['그리스', '아테네', '독일', '베를린', '러시아', '모스크바', '미국', '워싱턴']
    for i in range(0,len(nation),2):
        f.write(nation[i]+"-"+nation[i+1]+"\n")

# 2
with open('연락처.txt','r') as f:
    buffer = f.read()
    n = buffer.count("011-")
    buffer = buffer.replace("011-","010-")

with open('연락처.txt','w') as f:
    f.write(buffer)

    print(f'총 {n}건의 011 데이터를 찾았습니다.'+'\n'+'모든 데이터를 수정했습니다.')