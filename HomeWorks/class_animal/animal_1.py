'''
1、自己写一个面向对象的例子：

比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）

创建子类【猫】，继承【动物类】，

复写父类的__init__方法，继承父类的属性，

添加一个新的属性，毛发=短毛，

添加一个新的方法， 会捉老鼠，

复写父类的‘【会叫】的方法，改成【喵喵叫】

创建子类【狗】，继承【动物类】，

复写父类的__init__方法，继承父类的属性，

添加一个新的属性，毛发=长毛，

添加一个新的方法， 会看家，

复写父类的【会叫】的方法，改成【汪汪叫】

调用 name== ‘main’：

创建一个猫猫实例

调用捉老鼠的方法

打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。

创建一个狗狗实例

调用【会看家】的方法

打印【狗狗的姓名，颜色，年龄，性别，毛发】。

2、使用yaml 来管理猫猫，狗狗的属性
'''


import yaml


class Animal:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def shout(self):
        print(f"{self.name} is shouting")

    def run(self):
        print(f"{self.name} is running")


class Cat(Animal):
    fur = "短毛"

    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)

    def skill(self):
        print(f"{self.name}会捉老鼠")

    def shout(self):
        print(f"{self.name}会喵喵叫")

class Dog(Animal):
    fur = "长毛"

    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)

    def skill(self):
        print(f"{self.name}会看家")

    def shout(self):
        print(f"{self.name}会旺旺叫")

if __name__ == '__main__':
    with open("./animal_datas.yaml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)

    # cat
    data_cat = datas['cat']
    cat_1 = Cat(data_cat['name'], data_cat['color'], data_cat['age'], data_cat['gender'])
    cat_1.skill()
    print(f"姓名：{cat_1.name}, 颜色：{cat_1.color}, 年龄：{cat_1.age}岁, 性别：{cat_1.gender}, 毛发：{cat_1.fur}, 捉到了老鼠")

    # dog
    data_dog = datas['dog']
    dog_1 = Dog(data_dog['name'], data_dog['color'], data_dog['age'], data_dog['gender'])
    dog_1.skill()
    print(f"姓名：{dog_1.name}, 颜色：{dog_1.color}, 年龄：{dog_1.age}岁, 性别：{dog_1.gender}, 毛发：{dog_1.fur}")
