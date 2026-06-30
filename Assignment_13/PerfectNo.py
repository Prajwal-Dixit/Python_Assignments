def Factors(value):
    Result = list()
    for i in range(1,value):
        if((value % i) == 0):
            Result.append(i)
    return Result

def Perfect(no):
    value = Factors(no)
    Sum = 0
    for No in value:
        Sum = Sum + No
    
    if(no == Sum):
        return True
    else:
        return False
    
def main():
    No = int(input("Enter a number"))
    Ret = Perfect(No)
    
    if(Ret == True):
        print("Number is perfect")
    else:
        print("Number is not perfect")

if __name__ == "__main__":
    main()