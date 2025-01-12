n=int(input("Enter the number:"))
s=0
for i in range(1,n+1):
    k=i
    fact=1
    while k>0:
        fact=fact*k
        k=k-1
    s=s+(i/fact)
print(s)