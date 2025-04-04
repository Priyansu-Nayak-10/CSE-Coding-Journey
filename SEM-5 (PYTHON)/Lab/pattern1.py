
'''
for i in range(10): #for 10 rows
    for j in range(i+1):
        print('*', end='')
    print() # to change the line

for i in range(10): #for 10 rows
    for j in range(10-i):
        print('*', end='')
    print() # to change the line
    

for i in range(10): #for 10 rows
    for j in range(i+1): # for row spaces
        print('', end=' ')
    for j in range(10-i):
        print('*', end='')
    print() # to change the line '''
    

for i in range(10): #for 10 rows
    for j in range(10-i-1):
        print('', end=' ')
    for j in range(i+1):
        print('*', end='')
    print() # to change the line 
    
    
