###         5
###       4 5
###     3 4 5
###   2 3 4 5
### 1 2 3 4 5

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
    i-=1
    print()
    