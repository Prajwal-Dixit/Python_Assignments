def Area(value1, value2):
    area = value1 * value2
    return area

def main():
    print("Enter length and breadth of the rectangle")
    length = float(input())
    breadth = float(input())

    Ret = Area(length, breadth)
    print("Area of the  rectangle is : ",Ret)

if __name__ == "__main__":
    main()