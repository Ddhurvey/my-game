
rang=int(input("Enter the value. :- "))
i=1
c=0
k=1
sum=0
while i<rang:
    while k<=i:
        if i%k==0:
            c+=1
        k+=1
    if c==2:
        print(i)
        sum+=1
    c=0
    k=1
i+=1
print(sum)