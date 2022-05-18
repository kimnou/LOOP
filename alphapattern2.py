### A A A A A
### B B B B
### C C C 
### D D 
### E

i=1
while i<=5:
    j=5
    while j>=i:
        print(chr(64+i),end=" ")
        j-=1
    i+=1
    print()