# coding = utf-8

# 抽象产品类1
class Dog():
    @staticmethod
    def sound():
        print("wang wang")

    def introduce(self):
        raise NotImplemented

# dog的具体产品类1
class RollDog(Dog):
    def introduce(self):
        print("my ear is roll", end=" ")
        self.sound()

# dog的具体产品类2
class StraightDog(Dog):
    def introduce(self):
        print("my ear is straight", end=" ")
        self.sound()


# 抽象工厂类
class PetStore():
    def choice_dog(self):
        raise NotImplemented

# 具体工厂类
class RollStore(PetStore):
    def choice_dog(self):
        return RollDog()

# 具体工厂类
class StraightStore(PetStore):
    def choice_dog(self):
        return StraightDog()



if __name__ == '__main__':
    rd = RollStore().choice_dog()
    rd.introduce()
    sd = StraightStore().choice_dog()
    sd.introduce()
   