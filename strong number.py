####write a program to check if a number is strong number or not.

num=int(input("enter number:"))
sum=0
n=num
while n>0:
    digit=n%10
    fact=1
    for i in range (1,digit+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if sum==num:
    print("strong number")
else:
    print("not a strong number")
