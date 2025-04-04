Python 3.8.10 (default, Jul 29 2024, 17:02:10) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: /home/student/2241014108/python/p19.py ===============
you win
>>> 
================ RESTART: /home/student/2241014108/python/p19.py ===============
3
5
8
>>> 
================ RESTART: /home/student/2241014108/python/p19.py ===============
dice1:  5
dice2:  2
sum:  7
you win
>>> 
================ RESTART: /home/student/2241014108/python/p19.py ===============
dice1:  4
dice2:  5
sum:  9
>>> 
================ RESTART: /home/student/2241014108/python/p19.py ===============
>>> roll()
(2, 5)
>>> 
================ RESTART: /home/student/2241014108/python/p19.py ===============
>>> roll()
(3, 5)
>>> 
================ RESTART: /home/student/2241014108/python/p19.py ===============
>>> x1, x2 = (1,3)
>>> x1
1
>>> x2
3
>>> 
================ RESTART: /home/student/2241014108/python/p19.py ===============
>>> roll()
(4, 6)
>>> 
================ RESTART: /home/student/2241014108/python/p19.py ===============
player has rolled 3+4=7
>>> 
================ RESTART: /home/student/2241014108/python/p19.py ===============
player has rolled 3+5=8

================ RESTART: /home/student/2241014108/python/p19.py ===============
player has rolled 6+6=12
>>> 
================ RESTART: /home/student/2241014108/python/p19.py ===============
player has rolled 1+5=6
players_point is: 6
player has rolled 3+4=7
player loses
>>> 
================ RESTART: /home/student/2241014108/python/p19.py ===============
player has rolled 2+2=4
players_point is: 4
player has rolled 6+5=11
player has rolled 4+3=7
player loses
>>> 
================ RESTART: /home/student/2241014108/python/p19.py ===============
player has rolled 4+1=5
players_point is: 5
player has rolled 5+3=8
player has rolled 6+1=7
player loses
>>> 
================ RESTART: /home/student/2241014108/python/p19.py ===============
player has rolled 3+3=6
players_point is: 6
player has rolled 2+1=3
player has rolled 1+3=4
player has rolled 1+6=7
player loses
>>> 
================ RESTART: /home/student/2241014108/python/p20.py ===============
>>> 
================ RESTART: /home/student/2241014108/python/p20.py ===============
Guess my number between 1 to 100056
Too low! try again.
Guess my number between 1 to 100034
Too low! try again.
Guess my number between 1 to 1000556
Too high! try again.
Guess my number between 1 to 1000200
Too low! try again.
Guess my number between 1 to 10004090
Too high! try again.
Guess my number between 1 to 1000300
Too high! try again.
Guess my number between 1 to 1000250
Too high! try again.
Guess my number between 1 to 100014
Too low! try again.
Guess my number between 1 to 1000230
Too low! try again.
Guess my number between 1 to 1000235
Too high! try again.
Guess my number between 1 to 1000233
congratulations! you guessed.
would you like to continue playing? (y/n)n
>>> import math
>>> math.pow(2,3)
8.0
>>> math.ceil(2.9)
3
>>> math.floor(2.9)
2
>>> math.sqrt(100)
10.0
>>> math.fabs(-2.8)
2.8
>>> def square(a=3):
	return a**2

>>> def sq(a=3):
	return a**2

>>> sq(4)
16
>>> def sq():
	return a**2

>>> sq(5)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#22>", line 1, in <module>
TypeError: sq() takes 0 positional arguments but 1 was given
>>> 
================ RESTART: /home/student/2241014108/python/p21.py ===============
150
>>> 
================ RESTART: /home/student/2241014108/python/p21.py ===============
>>> product(2,3)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#23>", line 1, in <module>
  File "/home/student/2241014108/python/p21.py", line 10, in product
    p*=v
UnboundLocalError: local variable 'p' referenced before assignment
>>> 
================ RESTART: /home/student/2241014108/python/p21.py ===============
>>> product(2,3)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#24>", line 1, in <module>
  File "/home/student/2241014108/python/p21.py", line 11, in product
    return p
NameError: name 'p' is not defined
>>> 
================ RESTART: /home/student/2241014108/python/p21.py ===============
>>> product(2,3)
6
>>> product(2,2,3)
12
>>> t=(1,2,3,4)
>>> print(t)
(1, 2, 3, 4)
>>> print(*t)
1 2 3 4
>>> s='HELLO'
>>> s.lower()
'hello'
>>> s.upper()
'HELLO'
>>> l=[1,2,3,4]
>>> type(l)
<class 'list'>
>>> l.append(10)
>>> l
[1, 2, 3, 4, 10]
>>> 