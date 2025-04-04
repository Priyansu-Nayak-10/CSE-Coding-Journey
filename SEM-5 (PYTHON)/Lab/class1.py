Python 3.8.10 (default, Jul 29 2024, 17:02:10) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=1
>>> y = 2
>>> y=1
>>> x+y
2
>>> z=x+y
>>> z
2
>>> _a=5
>>> a_5 = 10
>>> 2a_=1
SyntaxError: invalid syntax
>>> variable =10
>>> Variable = 10
>>> variable = 20
>>> variable == Variable
False
>>> total = 10.8 +12 +8
>>> total
30.8
>>> 1-3
-2
>>> 2*6
12
>>> 12/5
2.4
>>> 10.0/5
2.0
>>> 10/5
2.0
>>> 10//5
2
>>> 10.0//5
2.0
>>> 2**3
8
>>> 12/5
2.4
>>> 12%5
2
>>> 10/0
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#25>", line 1, in <module>
ZeroDivisionError: division by zero
>>> (1+2*(1-3))
-3
>>> 2**3**2
512
>>> 1+(2*3**2//3/(1-3))
-2.0
>>> 3*(4-5)
-3
>>> 3*4-5
7
>>> 4**3**2
262144
>>> (4**3)**2
4096
>>> 4**(3**2)
262144
>>> print("welcome to python")
welcome to python
>>> for x in range(5):
	print(x)

	
0
1
2
3
4
>>> for x in range(5):
	print(x,end='')

	
01234
>>> for x in range(5):
	print(x,end=' ')

	
0 1 2 3 4 
>>> print("welcome to", "python")
welcome to python
>>> x = 2
>>> y=3
>>> print("the value of x+y=", x+y)
the value of x+y= 5
>>> print("this is the first line.\n this is the second line.")
this is the first line.
 this is the second line.
>>> print("this is the first.\n\n this is second.")
this is the first.

 this is second.
>>> print("a\tb")
a	b
>>> print("this is the backslash:","\")
      
SyntaxError: EOL while scanning string literal
>>>  print("this is the backslash:","\\")
 
SyntaxError: unexpected indent
>>> print("this is the backslash:","\")
      
SyntaxError: EOL while scanning string literal
>>> print("this is the backslash:","\\")
this is the backslash: \
>>> print("'","hii",",")
' hii ,
>>> print("'","hii","'")
' hii '
>>> print(""","hii",""")
,"hii",
>>> print("\'hi\'",'\"hi\"')
'hi' "hi"
>>> print("this is the first part of the text\")
      
SyntaxError: EOL while scanning string literal
>>> print("this is the first part of the text\
this is the second part of the text")
this is the first part of the textthis is the second part of the text
>>> type(5)
<class 'int'>
>>> type('string')
<class 'str'>
>>> print("""hello""")
hello
>>> s='''this is triple single quotes.'''
>>> type(s)
<class 'str'>
>>> s="""this is triple single quotes."""
>>> type(s)
<class 'str'>
>>> s="""this is triple double quotes."""
>>> type(s)
<class 'str'>
>>> s = '''this is the first line.
this is the second line.
this is the third line.'''
>>> s
'this is the first line.\nthis is the second line.\nthis is the third line.'
>>> """ 'hi' and "hi" """
' \'hi\' and "hi" '
>>> print("""This is a lengthy
multiline string containing
a few lines \
of text""")
This is a lengthy
multiline string containing
a few lines of text
>>> print("""This is a lengthy
   multiline string containing
a few lines \
of text""")
This is a lengthy
   multiline string containing
a few lines of text
>>> x=input("enter a number: ")
enter a number: 5
>>> type(x)
<class 'str'>
>>> y=int(x)
>>> y
5
>>> type(x)
<class 'str'>
>>> x
'5'
>>> n1 = int(input("enter the first number: "))
enter the first number: 21
>>> type(n1)
<class 'int'>
>>> n2 = int(input("enter the second number"))
enter the second number4
>>> print("the sum of two numbers is = ",n1+n2)
the sum of two numbers is =  25
>>> 
================ RESTART: /home/student/2241014108/python/p1.py ================
enter the first number: 21
enter the second number1
the sum of two numbers is =  22
>>> 
================ RESTART: /home/student/2241014108/python/p1.py ================
enter the first number: 21
enter the second number: 1
the sum of two numbers is =  22
>>> 
================ RESTART: /home/student/2241014108/python/p1.py ================
enter the first number: 21
enter the second number: 1
the sum of two numbers is =  22 .
>>> 
================ RESTART: /home/student/2241014108/python/p1.py ================
enter the first number: 21
enter the second number: 3
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/student/2241014108/python/p1.py", line 3, in <module>
    print("the sum of two numbers is = "+n1+n2+".")
TypeError: can only concatenate str (not "int") to str
>>> 
================ RESTART: /home/student/2241014108/python/p1.py ================
enter the first number: 23
enter the second number: 2
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "/home/student/2241014108/python/p1.py", line 3, in <module>
    print("the sum of two numbers is = "+(n1+n2)+".")
TypeError: can only concatenate str (not "int") to str
>>> 'a'+'b'
'ab'
>>> 
================ RESTART: /home/student/2241014108/python/p1.py ================
enter the first number: 22
enter the second number: 3
the sum of two numbers is = 25.
>>> 