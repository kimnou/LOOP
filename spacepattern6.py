###         5
###       5 4
###     5 4 3
###   5 4 3 2
### 5 4 3 2 1

i=5
while i>=1:
    j=1
    while j<=i:
        print(" ",end=" ")
        j+=1
    a=5
    while a>=i:
        print(a,end=" ")
        a-=1
    print()
    i-=1