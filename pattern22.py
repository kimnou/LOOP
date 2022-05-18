### 1
### 3  2
### 6  5  4
### 10 9  8  7

# n=5
# k=0
# for i in range(1,n):
#     k+=i
#     for j in range(k,k-i,-1):
#         print(str(j)+"",end=" ")
#     print()

i=1
while i<=1:
    print(i)
    i+=1
    j=3
    while j>=i:
        print(j,end=" ")
        j-=1
    print()
    k=6
    while k>=j+2:
        print(k,end=" ")
        k-=1
    print()
    l=10
    while l>=k+5:
        print(l,end="  ")
        l-=1
   

       

