# coding = utf-8
"""
    适配者模式目的： 让不属于同一抽象类的某个类，可以通过此抽象类的调用方式调用
    方式： 适配器类一般就是继承接口，然后实例化适配者对象，使其兼容。可以使调用同样的接口就解决问题
    好处： 不用改变原来的类，而是新增一个设配器类

    适配者模式为了兼容而存在： 把一不一样的接口变得一样
    具体场景：
        接口：  你现在有三孔跟两孔插座。或者说你有这几个类的实现代码，你可以通过这几个接口给很多东西充电，但是你不能直接给手机充电
        设配者： 手机，或者具体的说是usb接口的充电线+手机。此对象算是充电线 + 手机的整体
        设配器： 所以你需要一个充电头，，把两孔的插座转化成usb插座。实例对象是充电头 + 充电线 + 手机的整体

        这样，你可以把设配器当成平常的其他电器，同样的只要插入两孔插口，就能充电了
"""

# 目的： 为了让旺财可以跟其他两只Cat一样可以通过调用sound()接口来实现自我介绍

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
    def __init__(self, obj):
        self.obj = obj

    def sound(self):
       self.obj.barking()

# 为了兼容更多接口以及更多种类对象
# 适配器实现方式2
class Adapter2(Cat):
    def __init__(self, obj, adaptee):
        # adaptee是适配者字典{属性名： 属性对象}
        self.obj = obj
        # 使用__dict__.update方法给类增加属性
        self.__dict__.update(adaptee)


if __name__ == '__main__':
    # 实现1的遍历
    a = [XiaoGuang(), XiaoHei()]
    wc = WangCai()
    a.append(Adapter1(wc))
    for i in a:
        i.sound()
    print("================================")
    b = [XiaoGuang(), XiaoHei()]
    b.append(Adapter2(wc, {"sound": wc.barking}))
    for i in b:
        i.sound()
    # 输出结果:        
    # i am xiaoguang miao
    # i am XiaoHei miao
    # i am wangcai wang
    # ================================
    # i am xiaoguang miao
    # i am XiaoHei miao
    # i am wangcai wang