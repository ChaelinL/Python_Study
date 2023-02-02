
#기본 예제 (p.149)
#1
# expr = input("계산식을 입력하세요 >>> ")
# result = eval(expr)
# print(expr+'='+str(result))

#2
money = 10000
bread = 3000
result = divmod(money, bread)

print(f"빵을 {result[0]}개 사고 {result[1]}원이 남았습니다.")

#3
names = ['James', 'Anne', 'Merry']
scores = [10, 20, 30]
for names, scores in zip(names, scores):
    print(f"{names}의 점수는 {scores}점입니다.")

#4
month = [31, 28, 31, 30, 31, 30, 30, 31, 30, 31, 30, 31]

for month, day in enumerate(month):
    print(f"{month+1}월 = {day}일")


#응용 예제 (p.160)
#1
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

for rainbow, color in enumerate(rainbow):
    print(f"무지개의 {rainbow+1}번째 색은 {color}입니다.")

#2
print("점수를 입력하세요. 더 이상 입력할 점수가 없으면 음수를 아무거나 입력하세요.")
exam = []

while True:
    score = (int(input("점수 입력 >>> ")))
    if not score>0:
        break
    exam.append(score)

print(f"평균 = {sum(exam)/len(exam)}, 최대 = {max(exam)}, 최소 = {min(exam)}")