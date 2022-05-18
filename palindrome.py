###check if a number is palindrome or not.

n=int(input("enter number:"))
temp=n
user=0
while n>0:
    digit=n%10
    user=user*10+digit
    n=n//10
if temp==user:
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")

