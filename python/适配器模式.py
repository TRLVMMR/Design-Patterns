# coding = utf-8

class Cat():
    # 接口
    def sound(self):
        raise NotImplemented

# 小光, 是一只猫
class XiaoGuang(Cat):
    def sound(self):
        print("i am xiaoguang miao")

# 小黑，是一只猫
class XiaoHei(Cat):
    def sound(self):
        print("i am XiaoHei miao")

# 设配者：旺财，是一只狗而不是一只猫
class WangCai():
    # 狗叫声
    def barking(self):
        print("i am wangcai wang")

# 适配器实现方式1
class Adapter1(Cat):
    def __init__(self):
        self.obj = WangCai()

    def sound(self):
       self.obj.barking()

# 为了兼容更多接口以及更多种类对象
# 适配器实现方式2
class Adapter2(Cat):
    def __init__(self, obj, adaptee):
        # adaptee是适配者字典
        self.obj = obj
        # 使用__dict__.update方法给类增加属性
        self.__dict__.update(adaptee)


if __name__ == '__main__':
    # 实现1的遍历
    for i in [XiaoGuang, XiaoHei, Adapter1]:
        ani = i()
        ani.sound()
    print("================================")
    a = [XiaoGuang(), XiaoHei()]
    wc = WangCai()
    a.append(Adapter2(wc, {"sound": wc.barking}))
    for i in a:
        i.sound()
    # 输出结果:        
    # i am xiaoguang miao
    # i am XiaoHei miao
    # i am wangcai wang
    # ================================
    # i am xiaoguang miao
    # i am XiaoHei miao
    # i am wangcai wang