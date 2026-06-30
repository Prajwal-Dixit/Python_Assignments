def ChkGreater(No1, No2):
	if(No1 > No2):
		return No1
	else:
		return No2
		
def main():
	value1 = int(input("Enter first number"))
	value2 = int(input("Enter second number"))

	Ret = ChkGreater(value1, value2)

	print("Greater number is : ", Ret)

if __name__ == "__main__":
	main()
