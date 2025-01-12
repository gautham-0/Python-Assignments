n=int(input("Enter the value of n"))
x=int(input("enter the value of the exponent"))
s=0
for i in range(1,n+1):
    s+=((x**i)/i)
print(s)