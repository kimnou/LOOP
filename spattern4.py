###             10
###          20 10
###       30 20 10
###    40 30 20 10
### 50 40 30 20 10

i=10
while i<=60:
    j=60
    while j>=i:
        print(" ",end="  ")
        j-=10
    a=10
    while a<j+10:
        print(i-a,end=" ")
        a+=10
    print()
    i+=10