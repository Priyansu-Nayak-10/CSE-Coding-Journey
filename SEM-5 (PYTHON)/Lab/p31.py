"""
l=[[1,2,3],[4,5,6]]
print( '  0  1  2')
print('---------')
for row,i in enumerate(l):
    print(f'{i}|', end='')
    for e in row:
        print(e, end='')
    print()
"""
"""
def rotate(x,y,z):
    return z,x,y
a,b,c='doug', 22,1984
a,b,c=rotate(a,b,c)
print(a,b,c)
a,b,c=rotate(a,b,c)
print(a,b,c)
a,b,c=rotate(a,b,c)
print(a,b,c)

"""


def lis(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    return sorted(l1)
l=[1,2,4,1,3,6]
print(lis(l))
