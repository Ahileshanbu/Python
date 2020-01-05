#numbers not divisible by 3 or 5

init = 1

while init <=100:
    if init%3!=0 and init%5!=0 :
        print(init,end=" ")
    init += 1



#Pattern

print()
i,j = 1,1

while i <=4:
    while j<=4:
        print("#",end=" ")
        j+=1
    j=1;
    i += 1;
    print()
