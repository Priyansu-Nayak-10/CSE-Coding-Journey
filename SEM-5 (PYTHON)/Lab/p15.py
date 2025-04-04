num=int(input("Enter a five digit number : "))
n1=num//10000
num=num%10000
n2=num//1000
num=num%1000
n3=num//100
num=num%100
n4=num//10
n5=num%10
print(n5,n4,n3,n2,n1)
if (n1==n5 and n2==n4):
    print("pallindrome")
else:
    print("not pallindrome")
