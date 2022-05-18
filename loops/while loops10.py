###take user input in a variable named n.
###take user input as many times as the value of n.
###finally, print the sum of all those numbers which you have taken as input.

n=int(input("enter the variable number"))
i=1
sum=0
while i>=0 and i<=n:
    num=int(input("enter the number"))
    if num>=0:
        sum=sum+num
        print(sum)
    i+=1