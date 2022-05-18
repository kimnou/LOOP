###PERFECT NUMBER - a positive integer that is equal to the sum of its
###positive divisors excluding the number itself.

###write a python program to check if a number is perfect number or not

# num=int(input("enter number:"))
# result=0
# for i in range(1,num):
#     if num%i==0:
#         result=result+i
# if result==num:
#     print(num, "is a perfect number")
# else:
#     print(num, "is not perfect number")

num=int(input("enter number:"))
i=1
sum=0
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==num:
    print(num, "is perfect number")
else:
    print(num,"is not perfect number")



