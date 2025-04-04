'''
from decimal import Decimal as d
p=1000
r=d('0.05')
for n in range(1,11):
    a=p*(1+r)**n
    print(f"{n}\t\t{a}")

x=0
while x<=20:
    x+=1
    if x%5==0:
        continue 
    print(x,end=' ')

for row in range(10):
	for column in range(10):
		print('<' if row%2==1 else '>', end=' ')
	print()
'''
for row in range(2):
	for column in range(7):
		print('@',end=' ')
	print()