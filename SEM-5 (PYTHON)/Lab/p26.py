def f(a):
    return a%2==0
def t(x):
    return 3*x
l=[1,3,2,5,6,4,7,8,3,1]
L=list(filter(f,list(map(t,l))))
print(L)

L1=list(filter(lambda x:x%2==0, list(map(lambda a:a*3,l))))
print(L1)
