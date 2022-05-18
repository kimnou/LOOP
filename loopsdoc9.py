###write a program to display all even numbers that fall between two numbers
###(exclusive of the numbers) by the user.

num1=int(input("enter first number:"))
num2=int(input("enter second number"))
i=1
for i in range(num1,num2):
    if i%2==0:
        print(i, end=",")
        i+=1
            
