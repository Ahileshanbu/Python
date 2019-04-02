\\sum of digits and reverse of a number

x = int (input ("Enter the number "))

num = x

count = 0

while (num>0) :
    count += num%10
    num //=10

print("The sum of digit ",count)

num = x

count = 0

while (num>0):
    count = count * 10 + num % 10
    num //=10

print("The reverse of a number is ",count)
