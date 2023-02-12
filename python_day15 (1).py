import random

# try -> 시도할 코드 (가장 첫 단에 올 수 있다)
# except -> 오류시 실행할 코드 (try 아래에 올 수 있다)
# else -> 오류가 안났을 때 실행할 코드 (except 아래에 올 수 있다)
# finally -> 오류가 났든 안났든 실행할 코드 (가장 끝 단에 올 수 있다)

try:
    int(input('숫자를 입력하시오 >>> '))
except ValueError:
    print('숫자만 입력하세요!')
else:
    print('정상적인 실행')
finally:
    print('finally')


# 응용 예제 (p. 306)
# 1
class Quiz:
    answer = ['경기도','강원도','충청도','전라도','경상도','제주특별자치도']

    @classmethod
    def challenge(cls):
        a = input('정답은? >>> ')
        if cls.answer.__contains__(a) == True:
            print('정답입니다.')
            cls.answer.remove(a)
            cls.challenge()
        else:
            raise Exception('틀렸습니다.')

try:
    print('우리나라의 6개 모든 도를 맞히는 퀴즈입니다. 하나씩 대답하세요.')
    Quiz.challenge()
except Exception as e:
    print(e)


# 2
class UpDown:
    def __init__(self):
        self.answer = random.randint(1, 100)
        self.count = 0

    def play(self):
        self.challenge()

    def challenge(self):
        self.count += 1
        i = int(input('입력(1~100) >>> '))
        try:
            if 1 <= i <= 100:
                if self.answer == i:
                    print(f'{self.count}번만의 정답입니다.')
                    return
                elif self.answer > i:
                    print('Up')
                else:
                    print('Down')
            else:
                raise Exception('1~100 사이만 입력하세요.')
        except Exception as e:
            print(e)
        self.challenge()

game = UpDown()
game.play()


# 3
class BankError(Exception):
    def __init__(self, message):
        super().__init__(message)

class BankAccount:
    def __init__(self, account, money):
        self.account = account
        self.money = money

    def deposit(self, money):
        if money <=0:
            raise BankError(f'{money} 입금 불가')
        else:
            self.money += money

    def withdraw(self, money):
        if money <=0:
            raise BankError(f'{money} 출금 불가')
        elif self.money < money:
            raise BankError('잔액이 부족합니다.')
        else:
            self.money -= money

    def transfer(self, bank, money):
        try:
            self.withdraw(money)
            bank.deposit(money)
        except BankError as e:
            print(e)

    def info(self):
        print(f'계좌번호: {self.account}')
        print(f'잔액: {self.money}')

me = BankAccount('012-34-34567', 10000)
you = BankAccount('111-34-52134', 5000)


try:
    me.deposit(1000)
    me.transfer(you, 2000)
except BankError as e:
    print(e)
finally:
    me.info()
    you.info()