x=int(input("enter month in numeric value in their respectve order:"))
if (x<=7 and x%2==0):
    print("there are 30 days in month")
elif (x<=12 and x%2!=0):
    print("there are 30 days in month")
elif (x>12):
    print("error")
else:
    print("there are 31 days in month")
