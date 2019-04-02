# Armstrong Number

num = int (input ("Enter the number "))

x = num
count = 0

while (x>0) :
    count += 1
    x //= 10

# print ("Length of a number is ",count)

x = num
result = 0

while (x>0) :
    t = 1
    for i in range(count):
        t  = t * (x%10)
    result += t
    x //= 10

if(result == num):
    print ("The given number is armstrong number")
else :
    print("The given number is not armstrong number")


"""

Enter the number 5
The given number is armstrong number
>>> 
============== RESTART: C:/Users/A709113/Documents/Python/8.py ==============
Enter the number 153
The given number is armstrong number
>>> 
============== RESTART: C:/Users/A709113/Documents/Python/8.py ==============
Enter the number 34
The given number is not armstrong number

"""
