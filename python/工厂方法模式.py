# coding = utf-8

# 抽象产品类
class Dog():
    @staticmethod
    def sound():
        print("wang wang")

    def introduce(self):
        raise NotImplemented

# 具体产品类1
class WangCai(Dog):
    def introduce(self):
        print("my name is WangCai")
        self.sound()

# 具体产品类2
class AHuang(Dog):
    def introduce(self):
        print("my name is AHuang")
        self.sound()

# 工厂类
class DogStore():
    def __init__(self):
        self.dog = Dog()

    def choice(self, name):
        self.dog = name
        self.dog.introduce()


if __name__ == '__main__':
    dog = DogStore()
    dog.choice(WangCai())
    print("=======================")
    dog.choice(AHuang())