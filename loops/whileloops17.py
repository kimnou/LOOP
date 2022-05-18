###take input of weights of 11 people and print their average
###and check whether average weight is a multiple of 5 or not.
###(that means when u div the average weight by 5, r=0)

n=11
i=1
total_weight=0
while i<=n:
    weight=int(input("enter the weight"))
    i+=1
    total_weight=weight+total_weight
print(total_weight)
average=total_weight/11
print(average)
if average%5==0:
    print("multiple of 5")
else:
    print("not multiple of 5")