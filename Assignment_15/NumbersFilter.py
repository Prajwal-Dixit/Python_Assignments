Check = lambda No : (No % 3 == 0 and No % 5 == 0)

def main():
    Data = [5,15,35,90,20,45,30]
    Ret = list(filter(Check, Data))
    print(Ret)
    
if __name__ == "__main__":
    main()