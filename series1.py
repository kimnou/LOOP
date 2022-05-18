### print the follwing series 
### 1+2+6+24+120+.....+n terms

num=int(input("enter number:"))
i=1
sum=1
while i<=num:
    sum=sum*i
    print(sum,end=" ")
    i+=1
