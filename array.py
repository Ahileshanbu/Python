from array import *

arr = array('i',[])

num = int ( input ("Enter the num "))

for i in range(num) :
    x = int ( input ("Enter the next value "))
    arr.append(x)

arr.reverse()

print (arr.count(2))

print(arr)
