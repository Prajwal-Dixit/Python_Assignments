def Grade(value):
    if(value >= 75):
        return "Distinction"
    elif(value >= 60 and value < 75):
        return "First Class"    
    elif(value >= 50 and value < 60):
        return "Second Class"    
    else:
        return "Fail"    

def main():
    print("Enter marks of the student")
    Marks = float(input())

    Ret = Grade(Marks)
    print("Grade of the stuent is : ",Ret)

if __name__ == "__main__":
    main()