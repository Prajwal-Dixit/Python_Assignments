def Pattern(No):
    for i in range(0,No):
        print("* " * No)

#--------------------------------------OR------------------------------------#
# for i in range(0, No):
#         for j in range(0, No):
#             print("* ", end = " ")
#         print()
#----------------------------------------------------------------------------#
    
def main():
    No = int(input("Enter a number"))
    Pattern(No)

if __name__ == "__main__":
    main()