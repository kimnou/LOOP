###         1
###       1 2
###     1 2 3
###   1 2 3 4
### 1 2 3 4 5

i=1
while i<=5:
    j=5
    while j>=i:
        print(" ",end=" ")
        j-=1
    a=1
    while a<=i:
        print(a,end=" ")
        a+=1
    print()
    i+=1