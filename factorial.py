###write a program to find the factorial of a number.

num=int(input("enter number:"))
result=1
for i in range(num,0,-1):
    result=result*i
print("factorial of", num, "is", result)