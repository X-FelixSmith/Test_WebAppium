'''
类的学习
属性，方法
私有
继承
self
'''

class Person:
    # 静态属性
    name = None
    age = 20
    gender = '男'
    # 私有属性
    __money = 20
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender



    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleepping")


class Writer(Person):
    skill:str

    def __init__(self, name, age, gender,skill):
        # self.name = name
        # self.age = age
        # self.gender = gender
        super().__init__(name,age,gender)
        self.skill = skill

    def write(self):
        print(f"{self.name} is writing")

    def skill_1(self):
        print(f"my skill is {self.skill}")





per1 = Person('zhangsan',20,'男')
print(per1.name)
per1.eat()

writer1 = Writer('zuojia',40,'女','good write')
print(writer1.name)
writer1.sleep()
writer1.write()
writer1.skill_1()