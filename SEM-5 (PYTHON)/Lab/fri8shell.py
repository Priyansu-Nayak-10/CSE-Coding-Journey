Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import copy
>>> L=[1,[1,2,3],'A']
>>> L_S=copy.copy(L)
>>> L_S
[1, [1, 2, 3], 'A']
>>> L_S[1][0]=10
>>> L_S
[1, [10, 2, 3], 'A']
>>> L
[1, [10, 2, 3], 'A']
>>> L_S[0]=100
>>> L_S
[100, [10, 2, 3], 'A']
>>> L
[1, [10, 2, 3], 'A']
>>> L_D=copy.deepcopy(L)
>>> L_D
[1, [10, 2, 3], 'A']
>>> L_D[1][0]=100
>>> L_D
[1, [100, 2, 3], 'A']
>>> L
[1, [10, 2, 3], 'A']
>>> LS=L[:]
>>> 
======= RESTART: /home/student/2241014108/python/p25.py ======
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/student/2241014108/python/p25.py", line 2, in <module>
    stack.append['purple']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> stack=[]
>>> 
======= RESTART: /home/student/2241014108/python/p25.py ======
['purple', 'black', 'blue']
>>> 
======= RESTART: /home/student/2241014108/python/p25.py ======
push: ['purple', 'black', 'blue']
pop: ['purple', 'black']
>>> 
======= RESTART: /home/student/2241014108/python/p25.py ======
push: ['purple', 'black', 'blue']
pop: ['purple', 'black']
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> 
======= RESTART: /home/student/2241014108/python/p25.py ======
push: ['purple', 'black', 'blue']
pop: ['purple', 'black']
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
>>> 
======= RESTART: /home/student/2241014108/python/p25.py ======
push: ['purple', 'black', 'blue']
pop: ['purple', 'black']
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
with condition [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
>>> 
======= RESTART: /home/student/2241014108/python/p25.py ======
push: ['purple', 'black', 'blue']
pop: ['purple', 'black']

 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
with condition [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
>>> I=iter(l)
>>> print(I)
<list_iterator object at 0x7fe8de785f40>
>>> print(next(I))
5
>>> print(next(I))
10
>>> 
KeyboardInterrupt
>>> print(next(I))
15
>>> print(next(I))
20
>>> print(next(I))
25
>>> print(next(I))
30
>>> print(next(I))
35
>>> print(next(I))
40
>>> print(next(I))
45
>>> print(next(I))
50
>>> print(next(I))
55
>>> print(next(I))
60
>>> print(next(I))
65
>>> print(next(I))
70
>>> print(next(I))
75
>>> print(next(I))
80
>>> print(next(I))
85
>>> print(next(I))
90
>>> print(next(I))
95
>>> print(next(I))
100
>>> print(next(I))
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#39>", line 1, in <module>
StopIteration
>>> g=(a for a in range(10) if a%2==0)
>>> print(g)
<generator object <genexpr> at 0x7fe8dc542970>
>>> for e in g:
	print(e)

	
0
2
4
6
8
>>> print(next(g))
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#45>", line 1, in <module>
StopIteration
>>> g=(a  for a in range(10) if a%2==0)
>>> lg=list(lg)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#47>", line 1, in <module>
NameError: name 'lg' is not defined
>>> lg=list(g)
>>> lg
[0, 2, 4, 6, 8]
>>> t = tuple(lg)
>>> t
(0, 2, 4, 6, 8)
>>> """filter, map and reduce"""
'filter, map and reduce'
>>> numbers=[10,3,7,1,9,4,2,8,5,6]
>>> 
>>> def is_odd(x):
	return x%2 !=0

>>> list(filter(is_odd, numbers))
[3, 7, 1, 9, 5]
>>> def is_even(x):
	return x%2==0

>>> list(filter(is_even,range(1,51)))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> def f(x):
	return 2*x

>>> list(map(f, range(1,11)))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> 
======= RESTART: /home/student/2241014108/python/p26.py ======
[False, False, False, False, False, False]
>>> 
======= RESTART: /home/student/2241014108/python/p26.py ======
[6, 18, 12, 24]
>>> 
======= RESTART: /home/student/2241014108/python/p26.py ======
[6, 18, 12, 24]
[6, 18, 12, 24]
>>> colors=['red','blue','green','white']
>>> colors=[s.lower() for s in colors]
>>> min(colors)
'blue'
>>> M=[[1,2,3],[4,5,6],[7,8,9]]
>>> M[1][2]
6
>>> 
======= RESTART: /home/student/2241014108/python/p27.py ======
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/student/2241014108/python/p27.py", line 2, in <module>
    for i in l:
NameError: name 'l' is not defined
>>> 
======= RESTART: /home/student/2241014108/python/p27.py ======
1 2 3 
4 5 6 
7 8 9 
>>> 
======= RESTART: /home/student/2241014108/python/p27.py ======
1 2 3 
4 5 6 
7 8 9 
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
>>> 
======= RESTART: /home/student/2241014108/python/p27.py ======
1 2 3 
4 5 6 
7 8 9 
1 2 3 
4 5 6 
7 8 9 
>>> 
======= RESTART: /home/student/2241014108/python/p28.py ======
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/student/2241014108/python/p28.py", line 6, in <module>
    colors=[tuple(random.random() for _ in ramge(3)) for _ in range(len(X))]
  File "/home/student/2241014108/python/p28.py", line 6, in <listcomp>
    colors=[tuple(random.random() for _ in ramge(3)) for _ in range(len(X))]
NameError: name 'ramge' is not defined
>>> 
======= RESTART: /home/student/2241014108/python/p28.py ======

======= RESTART: /home/student/2241014108/python/p28.py ======
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/student/2241014108/python/p28.py", line 8, in <module>
    plt.Xlabel('x')
AttributeError: module 'matplotlib.pyplot' has no attribute 'Xlabel'
>>> 
======= RESTART: /home/student/2241014108/python/p28.py ======
>>> 