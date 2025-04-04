from random import randrange as rr
n1=rr(0,10)
n2=rr(0,10)
print(f"How much is {n1} times {n2}? ")
ans=n1*n2
res=int(input("Enter your answer"))
while ans!=res:
    print("No. Please try again")
    res=int(input("Enter your answer"))
print("Very Good")

