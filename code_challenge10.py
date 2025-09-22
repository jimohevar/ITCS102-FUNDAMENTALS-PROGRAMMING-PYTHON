for i in range(1,11,1):
    for y in range(10,i,-1):
        print(" ",end=' ')
    for z in range(1,i,1):
       print("*",end=" ")
    for x in range(1,i,1):
       print("*",end=" ")
    print()