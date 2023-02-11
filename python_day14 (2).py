
# 생성자와 소멸자
class Pizza:
    def __init__(self, x): # 객체 생성 시 자동으로 호출되는 메소드
        print('피자 완성')

    def __del__(self): # 객체 소명 시 자동으로 호출되는 메소드
        print('피자 버림')

Pizza() # 객체를 python이 없애는 순간 = 오래 안쓰는 경우


# 클래스 메소드와 정적 메소드

# self -> instance(생성된 객체) 접근
# cls -> class 접근

class Pizza:
    material = '불고기' # 클래스 변수 (self.이 아니라 cls.)

    # instance method
    def set_material(self, material):
        self.material = material

    # 객체 생성을 하지 않아도 실행 가능하다.
    @classmethod
    def set_material_cls(cls, material):
        cls.material = material

    # 클래스 변수, 인스턴스 변수에 접근할 수 없음
    # 객체 생성을 하지 않아도 실행 가능하다.
    @staticmethod
    def make_pizza():
        return Pizza()

p = Pizza()
p.set_material_cls('하와이안')
print(Pizza.material)


# pizza를 만들 때마다 몇 개인지 세는 클래스

class Pizza:
    count = 0

    def __init__(self):
        Pizza.count += 1

Pizza()
Pizza()
Pizza()
print(Pizza.count)


# 상속
# self -> 생성된 객체(자신)
# cls -> 클래스 객체
# super -> 부모 객체
class NameClass:
    def print_name(self):
        print('몰라용')

class A(NameClass):
    # 오버라이딩 -> 상속받은 객체의 메소드를 덮어씌운다
    def print_name(self):
        print('a')

class B(NameClass):
    pass

A().print_name()
B().print_name()


# isinstance(생성된객체, 클래스명) -> True or False 반환. 생성된 객체가 오른쪽의 클래스와 같니?
print(isinstance(A(),A))
print(isinstance(A(),B))
print(isinstance(A(),NameClass))


# 기본 예제 (p.286)
class Coffee:
    def __init__(self, bean):
        self.bean = bean

    def coffee_info(self):
        print(f'원두 : {self.bean}')

class Espresso(Coffee):
    def __init__(self, bean, water):
        super().__init__(bean)
        self.water = water

    # 오버라이딩
    def coffee_info(self):
        super().coffee_info()
        print(f'물 : {self.water}ml')

coffee = Espresso('콜롬비아', 30)
coffee.coffee_info()


# 기본 예제 (p.287)
# 1
# 이름-인스턴스변수, 전체 인구-클래스변수
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        print(f'{name} is born.')
        Person.count += 1

    @classmethod
    def get_population(cls):
        return cls.count

    def __del__(self):
        print(f'{self.name} is dead.')
        Person.count -= 1


# from 파일명 import Person
#
# man = Person('james')
# woman = Person('emily')
#
# print(f'전체 인구수 {Person.get_population()}명')
# del man
#
# print(f'전체 인구수 {Person.get_population()}명')


# 2
class Shop:
    total = 0
    menu_list = {'떡볶이':3000,'순대':3000,'튀김':500,'김밥':2000}

    @classmethod
    def sales(cls, name, amount):
        cls.total += cls.menu_list[name] * amount

# from 파일명 import Shop
# Shop.sales('떡볶이',1)
# Shop.sales('김밥',2)
# Shop.sales('튀김',5)
#
# print(f'매출: {Shop.total}원')


#3
class Car:
    max_oil = 50
    def __init__(self, oil):
        self.oil = oil

    def add_oil(self, oil):
        if oil <= 0:
            return

        self.oil += oil
        if self.oil > Car.max_oil:
            self.oil = Car.max_oil

    def car_info(self):
        print(f'현재 주유상태: {self.oil}')

class Hybrid(Car):
    max_e = 30
    def __init__(self, battery, oil):
        self.battery = battery
        super().__init__(oil)

    def charge(self, battery):
        if battery <= 0:
            return
        self.battery += battery
        if self.battery > Hybrid.max_e:
            self.battery = Hybrid.max_e

    def hybrid_info(self):
        super().car_info()
        print(f'현재 충전상태 : {self.battery}')

# from 파일명 import *
#
# car = Hybrid(0,0)
# car.add_oil(100)
# car.charge(50)
# car.hybrid_info()