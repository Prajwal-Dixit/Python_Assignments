class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def accept(self):
        self.Radius = float(input("Enter radius of the circle"))

    def area(self):
        self.Area = 2 * Circle.PI * self.Radius * self.Radius

    def circumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def display(self):
        print(f"Radius : {self.Radius}, Area : {self.Area}, Circumference : {self.Circumference}")

cobj1 = Circle()
cobj1.accept()
cobj2 = Circle()
cobj2.accept()

cobj1.area()
cobj1.circumference()
cobj1.display()

cobj2.area()
cobj2.circumference()
cobj2.display()
