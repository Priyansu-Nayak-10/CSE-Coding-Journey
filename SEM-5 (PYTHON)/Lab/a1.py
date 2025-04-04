Python 3.8.10 (default, Jul 29 2024, 17:02:10) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> L=[1, 2, 3, 4, 5, 6, 7]
>>> L[2:5]
[3, 4, 5]
>>> L[:5]
[1, 2, 3, 4, 5]
>>> L[2:]
[3, 4, 5, 6, 7]
>>> ls=L[3:]
>>> ls
[4, 5, 6, 7]
>>> L
[1, 2, 3, 4, 5, 6, 7]
>>> nl
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#7>", line 1, in <module>
NameError: name 'nl' is not defined
>>> nl=L[:]
>>> nl
[1, 2, 3, 4, 5, 6, 7]
>>> L[1:5:2]
[2, 4]
>>> L[1:6:2]
[2, 4, 6]
>>> L[::-1]
[7, 6, 5, 4, 3, 2, 1]
>>> L[-1:-8:-1]
[7, 6, 5, 4, 3, 2, 1]
>>> L[-2:-7:-2]
[6, 4, 2]
>>> L[::-3]
[7, 4, 1]
>>> L::-3
SyntaxError: invalid syntax
>>> L
[1, 2, 3, 4, 5, 6, 7]
>>> L[0:3]=['A','B','C']
>>> L
['A', 'B', 'C', 4, 5, 6, 7]
>>> L[1:3]=[]
>>> L
['A', 4, 5, 6, 7]
>>> L[:]=[]
>>> L
[]
>>> L[:]=[1,2,3,4,5,6,7,8,9]
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> t=(1,2,3)
>>> t
(1, 2, 3)
>>> l=list(t)
>>> l
[1, 2, 3]
>>> a=list(range(1,102))
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101]
>>> del a[22]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101]
>>> del a[21]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101]
>>> del a[:]
>>> a
[]
>>> L=[1,4,3]
>>> def f(l):
	l[0]=10
	return l

>>> f(L)
[10, 4, 3]

>>> L
[10, 4, 3]
>>> t=tuple(L)
>>> t
(10, 4, 3)
>>> def f(t)
SyntaxError: invalid syntax
>>> def f(t):
	l=list(t)
	l[0]=100
	return tuple(l)

>>> f(T)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#53>", line 1, in <module>
NameError: name 'T' is not defined
>>> f(t)
(100, 4, 3)
>>> 
>>> 
>>> L
[10, 4, 3]
>>> L=[3,1,7,10,5,2,9]
>>> L.sort()
>>> L
[1, 2, 3, 5, 7, 9, 10]
>>> L.sort(reverse=True)
>>> L
[10, 9, 7, 5, 3, 2, 1]
>>> L=[3,1,7,10,5,2,9]
>>> L_new=sorted(L)
>>> L_new
[1, 2, 3, 5, 7, 9, 10]
>>> l_new=sorted(L,reverse=True)
>>> l_new
[10, 9, 7, 5, 3, 2, 1]
>>> L.index(5)
4
>>> L=[3,5,1,2,5]
>>> L.index(5)
1
>>> L *=2
>>> L
[3, 5, 1, 2, 5, 3, 5, 1, 2, 5]
>>> L.index(5,6)
6
>>> t=('red','blue','purple','black')
>>> 'red' in t
True
>>> 'red' not in t
False
>>> numbers=list(range(1,11))
>>> 5 in numbers
True
>>> 11 i numbers
SyntaxError: invalid syntax
>>> 11 in numbers
False
>>> numbers.index(11)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#81>", line 1, in <module>
ValueError: 11 is not in list
>>> numbers.index(4)
3
>>> key=11
>>> for key in numbers:
	if key in numbers:
		print(f"The index of {key} is {numbers.index(key)}")
	else:
		print("Index not found.")

		
The index of 1 is 0
The index of 2 is 1
The index of 3 is 2
The index of 4 is 3
The index of 5 is 4
The index of 6 is 5
The index of 7 is 6
The index of 8 is 7
The index of 9 is 8
The index of 10 is 9
>>> 
======================================================== RESTART: /home/student/2241014108/python/q3.py ========================================================
The index of 1 is 0
The index of 2 is 1
The index of 3 is 2
The index of 4 is 3
The index of 5 is 4
>>> 
======================================================== RESTART: /home/student/2241014108/python/q3.py ========================================================
The index of 1 is 0
The index of 2 is 1
The index of 3 is 2
The index of 4 is 3
The index of 5 is 4
>>> 
======================================================== RESTART: /home/student/2241014108/python/q3.py ========================================================
Index not found.
>>> 