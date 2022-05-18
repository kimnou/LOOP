### A
### B B
### C C C
### D D D D
### E E E E E

i=1
while i<=5:
    j=1
    while j<=i:
        print(chr(64+i),end=" ")
        j+=1
    i+=1
    print()