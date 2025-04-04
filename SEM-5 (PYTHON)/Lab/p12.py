problem=input("What is your problem: ")
answer=input("Have you had this problem before?(yes or no): ")
if answer=='yes' or answer=='YES':
    print("Well, you have it again")
elif answer=='no' or answer=='NO':
    print("Well, you have it now")
else:
    print("Invalid input")