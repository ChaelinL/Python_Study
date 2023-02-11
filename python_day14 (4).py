
# 기본 예제 (p.276)
class USB:
    def __init__(self, capacity):
        self.capacity = capacity
    def info(self):
        print(f'{self.capacity}GB USB')

usb = USB(64)
usb.info()

# 기본 예제 (p.277)
class Service:
    def __init__(self, service):
        self.service = service
        print(f'{service} Service가 시작되었습니다.')

    def __del__(self):
        print(f'{self.service} Service가 종료되었습니다.')

s = Service('길 안내')
del s


# 기본 예제 (p. 282)
class Bag:

    count = 0

    def __init__(self):
        Bag.count += 1
    @classmethod
    def sell(cls):
        cls.count -= 1
    @classmethod
    def remain_bag(cls):
        return cls.count

print(f'현재 가방: {Bag.remain_bag()}개')
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
print(f'현재 가방: {Bag.remain_bag()}개')
bag1.sell()
bag2.sell()
print(f'현재 가방: {Bag.remain_bag()}개')


# 기본 예제 (p.286)
class Coffee:
    def __init__(self,bean):
        self.bean = bean
    def coffee_info(self):
        print(f'원두: {self.bean}')

class Espresso(Coffee):
    def __init__(self,bean,water):
        super().__init__(bean)
        self.water = water
    def espresso_info(self):
        super().coffee_info()
        print(f'물: {self.water}ml')

coffee = Espresso('콜롬비아', 30)
coffee.espresso_info()


# 응용 예제 (p.287)
# 1
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

man = Person('james')
woman = Person('emily')

print(f'전체 인구수: {Person.get_population()}')
del man
print(f'전체 인구수: {Person.get_population()}')


# 2
class Shop:
    total = 0
    menu_list = {'떡볶이':3000,'순대':3000,'튀김':500,'김밥':2000}

    @classmethod
    def sales(cls, name, count):
        cls.total += cls.menu_list[name]*count

Shop.sales('떡볶이',1)
Shop.sales('김밥',2)
Shop.sales('튀김',5)

print(f'매출: {Shop.total}원')


# 3
class Car:
    max_oil = 50

    def __init__(self,oil):
        self.oil = oil

    def add_oil(self,oil):
        if oil <= 0:
            return
        self.oil += oil
        if self.oil > Car.max_oil:
            self.oil = Car.max_oil

    def car_info(self):
        print(f'현재 주유상태: {self.oil}')

class Hybrid(Car):
    max_electric = 30
    def __init__(self,electric,oil):
        self.electric = electric
        super().__init__(oil)

    def charge(self,electric):
        if electric <= 0:
            return
        self.electric += electric
        if self.electric > Hybrid.max_electric:
            self.electric = Hybrid.max_electric

    def hybrid_info(self):
        super().car_info()
        print(f'현재 충전상태: {self.electric}')

car = Hybrid(0,0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()