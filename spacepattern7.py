###         5
###       4 4
###     3 3 3
###   2 2 2 2
### 1 1 1 1 1

i=5
while i>=1:
    j=1
    while j<=i:
        print(" ",end=" ")
        j+=1
    a=5
    while a>=i:
        print(i,end=" ")
        a-=1
    print()
    i-=1