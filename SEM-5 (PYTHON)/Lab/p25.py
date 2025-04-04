"""push pop"""
stack=[]
stack.append('purple')
stack.append('black')
stack.append('blue')
print("push:",stack)
stack.pop()
print("pop:",stack)

""" list comprehsion"""
l=[i for i in range(1,101)]
print(l)

l=[i for i in range(1,101) if i%5==0]
print("with condition",l)

