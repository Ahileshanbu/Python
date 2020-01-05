#Leap year or not

num = int(input("Enter the Year: "))

if num%4==0 :
    if num%100 == 0:
        if num%400 == 0:
            print("Given year is leap year")
        else :
            print("Given year is not a leap year")
    else:
        print("Given year is leap year")
else:
    print("Given year is not a leap year")



#Positive or not

num = int(input("Enter the number: "))

if num>0:
    print("Given number is Positive")
elif num<0:
    print("Given number is Negative")
else:
    print("Given number is Zero")




#Largest number

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
num3 = int(input("Enter the num3: "))

if num1>num2 and num1>num3 :
    print(num1, "is greater")
elif num2>num1 and num2>num3 :
    print(num2, "is greater")
else:
    print(num3, "is greater")
