####write a program to print a table of a number entered by the user.

num=int(input("enter number:"))
i=1
for i in range (1,11):
    table=num*i
    print(num,"*",i,"=",table)
    i+=1