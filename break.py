" use of break statement" 
i=1
while i<=3:
    x=int(input("enter an even no"))
    if x%2==0:
        break
    else:
        i+=1
if i==4:
    print("you lost")
else:
    print("you win")

    
