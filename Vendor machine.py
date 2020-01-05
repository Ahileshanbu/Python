totalpencil = 10
totaleraser = 10

pencil = int(input("Enter the no of Pencil you want: "))
eraser = int(input("Enter the no of eraser you want: "))

i = 1

if pencil > totalpencil :
    print("We do have only ",totalpencil," Pencils available in store")
else:
    while i<=pencil:
        print("Pencil",end=" ")
        i+=1
    totalpencil -= pencil
    print()
    i = 1

if eraser > totaleraser :
    print("We do have only ",totaleraser," Erasers available in store")
else:
    while i<= eraser:
        print("Eraser",end=" ")
        i+=1
    totaleraser -= eraser
    print()

print("Available no of Pencil:",totalpencil)
print("Available no of Eraser:",totaleraser)
