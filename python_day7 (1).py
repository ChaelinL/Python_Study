
#break - 반복문 탈출 명령
#continue - 반복문의 다음 동작으로 넘어가는 명령

for i in range(10):
    if i ==5:
        continue
    print(i)


#응용 예제 (p.141)
#2
while True:
    a = int(input('이번 영화의 평점을 입력하세요 >>> '))
    if 1<= a <=5:
        print('★'*a)
        break
    print('평점은 1~5 사이만 입력할 수 있습니다.')

#4
for i in range(3, 10):
    if i%2==0:
        print()
        continue
    for j in range(1, i+1):
        print(f'{i}x{j}={i*j}')
