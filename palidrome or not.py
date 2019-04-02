# Palindrome or not

num = int ( input ("Enter the number "))

x = num
result = 0

while (x > 0) :
    result = (result * 10) + x%10
    x //= 10

if result == num :
    print ("The given number is a palidrome ")
else :
    print ("The given number is not a palindrome ")

"""

Enter the number 23
The given number is not a palindrome 
>>> 
============== RESTART: C:/Users/A709113/Documents/Python/10.py ==============
Enter the number 22
The given number is a palidrome 
>>> 
============== RESTART: C:/Users/A709113/Documents/Python/10.py ==============
Enter the number 120
The given number is not a palindrome 
>>> 
============== RESTART: C:/Users/A709113/Documents/Python/10.py ==============
Enter the number 1
The given number is a palidrome

"""
    
