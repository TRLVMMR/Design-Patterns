# coding = utf-8


# 抽象产品类1
class Dog():
    @staticmethod
    def sound():
        print("wang wang")

    def introduce(self):
        raise NotImplemented

# dog的具体产品类1
class StraightDog(Dog):
    def introduce(self):
        print("my ear is straightdog", end=" ")
        self.sound()

# dog的具体产品类2
class RollDog(Dog):
    def introduce(self):
        print("my ear is rolldog", end=" ")
        self.sound()

# 抽象产品类2
class Cat():
    @staticmethod
    def sound():
        print("miao miao")

    def introduce(self):
        raise NotImplemented

# cat的具体产品类1
class RollCat(Cat):
    def introduce(self):
        print("my ear is roll", end=" ")
        self.sound()

# cat的具体产品类2
class StraightCat(Cat):
    def introduce(self):
        print("my ear is straight", end=" ")
        self.sound()

# 抽象工厂类
class PetStore():

    def choice_dog(self):
        raise NotImplemented

    def choice_cat(self):
        raise NotImplemented

# 直耳具体工厂类
class StraightStore():

    def choice_dog(self):
        return StraightDog()

    def choice_cat(self):
        return StraightCat()

# 卷耳具体工厂类
class RollStore():

    def choice_dog(self):
        return RollDog()

    def choice_cat(self):
        return RollCat()


if __name__ == '__main__':
    dog = StraightStore()
    d = dog.choice_dog()
    d.introduce()
    d = dog.choice_cat()
    d.introduce()
    print("====================")
    cat = RollStore()
    c = cat.choice_dog()
    c.introduce()
    c = cat.choice_cat()
    c.introduce()
   