class Demo:
    Value = 0
    def __init__(self, A, B):
        self.No1 = A
        self.No2 = B
    
    def fun(self):
        print(f"No1 : {self.No1}, No2 : {self.No2}")

    def gun(self):
        print(f"No1 : {self.No1}, No2 : {self.No2}")

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.fun()
obj2.fun()

obj1.gun()
obj2.gun()
