'''
n="*"
for x in range(10):
    print(n)
    n+='*' 
    '''
n = 10 

for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * i)

