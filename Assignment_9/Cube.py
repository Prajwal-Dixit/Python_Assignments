def Cube(value):
    Result = value * value * value
    return Result

def main():
	No = int(input("Enter the number"))
	
	Ret = Cube(No)

	print("Cube of the number is : ", Ret)

if __name__ == "__main__":
	main()
