" check whether no is prime or not in range"

a=int(input("enter smaller no"))
b=int(input("enter larger no"))
s=range(a,b)
for x in s:
    for num in range(2,x):
        if x%num==0:
            break
    else:
        print(x," is prime no")
        
