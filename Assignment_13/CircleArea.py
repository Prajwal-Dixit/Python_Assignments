from math import pi

def Area(value):
    area = pi * value * value 
    return area

def main():
    print("Enter radius of the circle")
    radius = float(input())

    Ret = Area(radius)
    print("Area of the  circle is : ",Ret)

if __name__ == "__main__":
    main()