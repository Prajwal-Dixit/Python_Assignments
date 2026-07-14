class Arithmatic:
    def __init__(self):
        self.Value1 = 0.0
        self.Value2 = 0.0

    def Accept(self):
        print("Enter two numbers")
        self.Value1 = float(input())
        self.Value2 = float(input())
    
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        try:
            return self.Value1 / self.Value2
        
        except ZeroDivisionError:
            print("Division by zero is not allowed, enter other numbers")

obj = Arithmatic()
obj.Accept()
add = obj.Addition()
sub = obj.Subtraction()
mult = obj.Multiplication()
div = obj.Division()

print("Addition is : ", add)
print("Subtraction is : ", sub)
print("Multiplication is : ", mult)
print("Division is : ", div)