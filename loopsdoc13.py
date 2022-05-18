###write a program to reverse a number accepted by the user.

num=int(input("enter number:"))
while num>0:
    num=num%10
    num=num//10
print(num)

