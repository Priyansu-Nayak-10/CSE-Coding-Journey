'''
import random
n=random.randrange(1,7)
m=random.randrange(1,7)
print("dice1: ",n)
print("dice2: ",m)
sum=n+m
print("sum: ",sum)
if(sum==7 or sum==11):
    print("you win")
elif(sum==2 or sum==3 or sum==12):
    print("you lose")
'''

from random import randrange as rr
def roll():
    d1=rr(1,7)
    d2=rr(1,7)
    return d1,d2
def display(dice): #dice=(2,1)
    d1, d2=dice  #unpacking
    print(f"player has rolled {d1}+{d2}={d1+d2}")
die_values = roll() # a tuple
display(die_values)
sum_of_s=sum(die_values)
if sum_of_s in (7,11):
    game_status = 'WON'
elif sum_of_s in (2,3,12):
    game_status = 'LOST'
else:
    game_status = 'CONTINUE'
    players_point = sum_of_s
    print(f"players_point is: {players_point}")

while game_status=='CONTINUE':
    die_values = roll()
    display(die_values)
    sum_of_s = sum(die_values)
    if sum_of_s == players_point:
        game_status = 'WON'
    elif sum_of_s == 7:
        game_status= 'LOST' 
if game_status =='WON':
    print(f"player wins.")
else:
    print(f"player loses")
