import random
import string
print("Welcome ! to our random password generator.")
def main():
    length=int(input("Enter the length of password you want: "))
    lowerD=string.ascii_lowercase
    upperD=string.ascii_uppercase
    digit=string.digits
    symbols=string.punctuation
    combine=lowerD + upperD + digit + symbols
    x=random.sample(combine,length)
    password="".join(x)
    print(password) 
    main()
main()