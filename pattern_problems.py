def a():
    for i in range(5,0,-1):
        for j in range(5,i-1,-1):
            print(j,end=" ")
        print()
    for i in range(2,6):
        for j in range(5,i-1,-1):
            print(j,end=" ")
        print()
a()    
def b():
    for i in range(1,6):
        for j in range(1,6-i):
            print(" ",end=" ")
        for k in range(1,2*i):
            print(k,end =" ")
        print()
    for i in range(4,0,-1):
        for j in range(1,6-i):
            print(" ",end=" ")
        for k in range(1,2*i):
            print(k,end=" ")
        print()
b()
