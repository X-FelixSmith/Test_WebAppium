def demo():
    for i in range(0,10):
        print("--------------")
        print("start!!!")
        yield i
        print("end!")
        print("______________")



p = demo()
print(next(p))
print(next(p))
print(next(p))
print(next(p))
