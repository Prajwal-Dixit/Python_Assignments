def Square(value):
    Result = value * value
    return Result

def main():
	No = int(input("Enter the number"))
	
	Ret = Square(No)

	print("Square of the number is : ", Ret)

if __name__ == "__main__":
	main()
