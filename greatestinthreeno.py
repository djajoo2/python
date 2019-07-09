x=int(input("enter 1st no."))
y=int(input("enter 2nd no."))
z=int(input("enter 3rd no."))
if (x>y and x>z):
    print("%d is greatest"%x)
elif (y>x and y>z):
    print("%d is greatest"%y)
else:
    print("%d is greatest"%z)
