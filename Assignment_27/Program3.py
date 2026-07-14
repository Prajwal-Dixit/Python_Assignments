class Numbers:
    def __init__(self):
        value = int(input("Enter a number"))
        self.Value = value

    def ChkPrime(self):
        for i in range(2, self.Value):
            if(self.Value % i == 0):
                return False
            else:
                return True
            
    def ChkPerfect(self):
        sum = 0
        for i in range(1, self.Value):
            if(self.Value % i == 0):
                sum += i
        if(sum == self.Value):
            return True
        else:
            return False
        
    def Factors(self):
        fact = []
        for i in range(1, self.Value+1):
            if(self.Value % i == 0):
                fact.append(i)
        return fact
    
    def SumFactors(self):
        fact = self.Factors()
        sum = 0
        for no in fact:
            sum += no
        return sum
    
obj1 = Numbers()
Ret1 = obj1.ChkPrime()
Ret2 = obj1.ChkPerfect()
Ret3 = obj1.Factors()
Ret4 = obj1.SumFactors()

print(f"Factors are : {Ret3}, Sum of all factors is : {Ret4}")
if(Ret1 == True):
    print("Number is Prime")
else:
    print("Number is not Prime")

if(Ret2 == True):
    print("Number is Perfect")
else:
    print("Number is not Perfect")