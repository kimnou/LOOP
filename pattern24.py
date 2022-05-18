### 1
### 2 3 4
### 5 6 7 8 9

start=1
stop=2
rows=3
for i in range(rows):
    for col in range(1,stop):
        print(start,end=" ")
        start+=1
    print("")
    stop+=2