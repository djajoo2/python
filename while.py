
x=1
while x<=5:
     print("dinesh")
     x+=1

x=1
while x<=10:
     print(x)
     x+=1
x=10
while x>=1:
     print(x)
     x-=1
print(x)

#print 10 odd natural no.
x=1
while x<20:
     print(x)
     x+=2
     
#print 10 even no
x=2
while x<=20:
     print(x)
     x+=2

#print n natural no.
n=int(input("enter no of terms"))
x=1
while x<=n:
     print(x)
     x+=1

#print n natural no in reverse order
n=int(input("enter no of terms"))
x=n
while x>=1:
     print(x)
     x-=1

#sum of n natural no
n=int(input("enter no of terms"))
sum=0
x=1
while x<=n:
     sum=sum+x
     x+=1
print(sum)


#sum of n odd natural no
n=int(input("enter no of terms"))
x=1
sum=0
while x<=n*2:
     sum=sum+x
     x+=2
print(sum)


#factorial of no
n=int(input("enter a no."))
fact=1
while n!=0:
     fact=fact*n
     n-=1
print(fact)


#product of n odd no
n=int(input("enter no of terms"))
x=1
mul=1
while x<=n*2:
   mul=mul*x
   x+=2
print(mul)
