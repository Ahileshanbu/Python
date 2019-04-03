# String manipulation

str = input ("Enter the string ")

print(id(str))

print(str[2:])

print("The length of a string is ",len (str))

print("The min of a string is ",min (str))

print("The max of a string is ",max (str))

print("The given string is alphabet ? ",str.isalpha())

print("The count of 'h' is ",str.count("o"))

print("Find the value 's' ",str.find('s'))

print("The capitalize of str ",str.capitalize())

print("The title os str is ",str.title())

print("To upper of str is ",str.upper())

print("The swapcase of str is ",str.swapcase())

"""

Enter the string Hi hoW are yoU
48920600
 hoW are yoU
The length of a string is  14
The min of a string is   
The max of a string is  y
The given string is alphabet ?  False
The count of 'h' is  2
Find the value 's'  -1
The capitalize of str  Hi how are you
The title os str is  Hi How Are You
To upper of str is  HI HOW ARE YOU
The swapcase of str is  hI HOw ARE YOu

"""
