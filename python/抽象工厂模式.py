# coding = utf-8

import random

# 抽象产品类1
class Dog():
    @staticmethod
    def sound():
        print("wang wang")

    def introduce(self):
        raise NotImplemented

# dog的具体产品类1
class WangCai(Dog):
    def introduce(self):
        print("my name is WangCai")
        self.sound()

# dog的具体产品类2
class AHuang(Dog):
    def introduce(self):
        print("my name is AHuang")
        self.sound()

# dog抽象产品类2
class Cat():
    @staticmethod
    def sound():
        print("miao miao")

    def introduce(self):
        raise NotImplemented

# cat的具体产品类1
class XiaoGuang(Cat):
    def introduce(self):
        print("my name is XiaoGuang")
        self.sound()

# cat的具体产品类2
class XiaoHei(Cat):
    def introduce(self):
        print("my name is XiaoHei")
        self.sound()

# 抽象工厂类
class PetStore():
    def __init__(self):
        self.pet = None

    def choice(self):
        raise NotImplemented

# 具体工厂类
class DogStore():
    def __init__(self):
        self.pet = Dog()

    def choice(self):
        for i in [WangCai, AHuang]:
            yield i
# 工厂类
class CatStore():
    def __init__(self):
        self.pet = Cat()

    def choice(self):
        for i in [XiaoGuang, XiaoHei]:
            yield i


if __name__ == '__main__':
    dog = DogStore()
    d = dog.choice()
    for i in d:
        i().introduce()

    cat = CatStore()
    c = cat.choice()
    for i in c:
        i().introduce()
   