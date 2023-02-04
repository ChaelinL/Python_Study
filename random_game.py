import random

# 업다운 게임
# 랜덤으로 컴퓨터가 1 ~ 100 사이의 숫자를 뽑습니다.
# 사용자는 총 5번 입력을 시도 (정수)

def up_down():
    ran = random.randint(1,100)
    for i in range (5):
        print(f"{i+1}번째 시도입니다.")
        num = int(input("1부터 100 사이의 숫자를 입력하세요 >>> "))
        if num == ran:
            print("정답입니다.")
            break

        if i == 4:
            print(f"정답은 {ran}입니다.")
            break

        if num > ran:
            print("down")
        else:
            print("up")
