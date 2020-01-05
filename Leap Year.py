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
