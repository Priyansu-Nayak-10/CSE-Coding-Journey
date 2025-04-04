
from random import randrange as rr
def guess():
    n=rr(1, 1001)
    m=int(input("Guess my number between 1 to 1000"))
    while m!=n:
        if m>n:
            print("Too high! try again.")
        else:
            print("Too low! try again.")
        m=int(input("Guess my number between 1 to 1000"))
    print("congratulations! you guessed.")
guess()
ans=input("would you like to continue playing? (y/n)")
while True:
    if ans=='y':
        guess()
    else:
        break
