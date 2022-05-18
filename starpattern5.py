###         *
###       * *
###     * * *
###   * * * *
### * * * * *

# i=1
# while i<=6:
#     j=5
#     while j>=i:
#         print(" ",end=" ")
#         j=j-1
#     n=i
#     while n>1:
#         print("*",end=" ")
#         n=n-1
#     print()
#     i=i+1

i=1
while i<=5:
    space=1
    while space <=5-i:
        print(" ", end=" ")
        space=space+1
    star = 1
    while star<=i:
        print("*", end=" ")
        star=star+1
    print()
    i=i+1