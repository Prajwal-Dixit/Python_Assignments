def ChkVowel(value):
    lower = "aeiou"
    upper = "AEIOU"

    for i in lower:
        if(i == value):
            return True
        
    for i in upper:
        if(i == value):
            return True

def main():
    Ret = False
    ch = input("Enter a letter")
    Ret = ChkVowel(ch)

    if(Ret == True):
        print("Its vowel")
    else:
        print("Its consonant")

if __name__ == "__main__":
    main()