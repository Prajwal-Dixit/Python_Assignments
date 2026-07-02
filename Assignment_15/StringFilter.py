Check = lambda str : (len(str) >= 5)

def main():
    Data = ["Python", "Data", "Machine", "Car", "Bike", "Learning"]
    Ret = list(filter(Check, Data))
    print(Ret)
    
if __name__ == "__main__":
    main()