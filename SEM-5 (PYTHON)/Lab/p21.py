'''def area(l, w=5):
    a =l*w
    return a
print(area(w=10, l=5))
'''

def product(a,*b):
    prod=a
    for v in b:
        prod*=v
    return prod
    
