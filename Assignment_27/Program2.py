class BankAccount:
    ROI = 10.5
    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print(f"Name : {self.Name}, current balance : {self.Amount}")

    def Deposit(self):
        deposit = int(input("Enter the amount you want to deposit"))
        self.Amount = self.Amount + deposit
    
    def Withdraw(self):
        amount = int(input("Enter the amount you want to withdraw"))
        if(amount > self.Amount):
            print("Sorry! You dont have sufficient balance")
        else:
            self.Amount = self.Amount - amount
    
    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest
    
obj1 = BankAccount("Mark", 1000)
obj2 = BankAccount("John", 300)
obj3 = BankAccount("Rakesh", 900)

obj1.Display()
obj2.Display()
obj3.Display()

obj1.Deposit()
obj2.Deposit()
obj3.Deposit()

obj1.Display()
obj2.Display()
obj3.Display()

Ret = obj1.CalculateInterest()
print(f"Interest for {obj1.Name} is :", Ret)

Ret = obj2.CalculateInterest()
print(f"Interest for {obj2.Name} is :", Ret)

Ret = obj3.CalculateInterest()
print(f"Interest for {obj3.Name} is :", Ret)