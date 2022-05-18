### 1
### B B
### 3 3 3
### D D D D
### 5 5 5 5 5

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         if i%2==0:
#             print(chr(64+i), end=" ")
#         else:
#             print(i, end=" ")
#         j+=1
#     print()
#     i+=1

i=1
while i<=5:
    j=5
    while j>=i:
        if i%2==0:
            print(chr(64+j), end=" ")
        else:
            print(j,end=" ")
        j+=1
    print()
    i-=1