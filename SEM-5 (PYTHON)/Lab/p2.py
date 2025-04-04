#maximum and minimum

'''n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number : "))
n3=int(input("enter the third number : "))
if(n1<n2):
    if(n1<n3):
        print("n1 is smaller")
    else:
        print("n3 is minimum")
else:
    if(n2<n3):
        print("n2 is minimum")
    else:
        print("n3 is minimum")

n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number : "))
n3=int(input("enter the third number : "))
min_=n1
if min_>n2:
    min_=n2
if min_>n3:
    min_=n3
print("minimum =", min_)'''

n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number : "))
n3=int(input("enter the third number : "))
min_=min(n1,n2,n3)
max_=max(n1,n2,n3)
print("minimum =",min_,"maximum =",max_)


