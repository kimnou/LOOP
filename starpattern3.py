###     *
###    * *
###   * * *
###  * * * *
### * * * * *

# i=5
# row=0
# while row<i:
#     space = i-row-1
#     while space>0:
#         print(end=" ")
#         space = space-1
#     star=row+1
#     while star>0:
#         print("*", end=" ")
#         star=star-1
#     row=row+1
#     print()

row=5
for i in range(1,row+1):
    print(" "*(row-i),end=" ")
    print("* "*i)

# i=1
# while i<=5:
#     space=1
#     while space<=5-i:
#         print("", end=" ")
#         space=space+1
#     star=1
#     while star<=i:
#         print("* ", end="")
#         star=star+1
#     print()
#     i=i+1