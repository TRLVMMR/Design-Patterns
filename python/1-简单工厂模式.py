# coding = utf-8
"""
    简单工厂模式：
        你要车，去工厂提更简单， 工厂里有所有车的产品，而不需要你自己从0造车
        工厂角色： 对产品进行加工建造，后返回产品
        抽象产品角色：如车，猫，狗
        具体产品角色：如奔驰，宝马。
"""

# 抽象产品类
class Dog():
    @staticmethod
    def sound():
        print("wang wang")

    def introduce(self):
        raise NotImplemented

# 具体产品类1
class StraightDog(Dog):
    def introduce(self):
        print("my ear is straight", end=" ")
        self.sound()

# 具体产品类2
class RollDog(Dog):
    def introduce(self):
        print("my ear is roll", end=" ")
        self.sound()

# 工厂类
class DogStore():
    @staticmethod
    def choice_dog(name):
        if name == "StraightDog":
            return StraightDog()
        elif name == "RollDog":
            return RollDog()
        return None


if __name__ == '__main__':
    dog = DogStore()
    dog.choice_dog("StraightDog").introduce()
    dog.choice_dog("RollDog").introduce()