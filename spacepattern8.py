###             10
###          10 20
###       10 20 30
###    10 20 30 40
### 10 20 30 40 50

i=10
while i<=50:
    j=50
    while j>=i:
        print(" ",end="  ")
        j-=10
    a=10
    while a<=j+10:
        print(a,end=" ")
        a+=10
    print()
    i+=10