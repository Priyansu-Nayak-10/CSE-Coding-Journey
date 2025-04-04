Python 3.8.10 (default, Jul 29 2024, 17:02:10) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(2, 10):
	print (i,end=' ')

	
2 3 4 5 6 7 8 9 
>>> for i in range(1, 10, 2):
	print(i, end=' ')

	
1 3 5 7 9 
>>> range(10)
range(0, 10)
>>> for i in range (10,0,-1):
	print(i,end=' ')

	
10 9 8 7 6 5 4 3 2 1 
>>> x=0.1
>>> y=0.2
>>> x+y
0.30000000000000004
>>> print(x+y:.2f)
SyntaxError: invalid syntax
>>> print(x+y)
0.30000000000000004
>>> import decimal
>>> from decimal import Decimal as d
>>> x=0.1
>>> y=0.2
>>> x+y
0.30000000000000004
>>> x=d('0.1')
>>> y=d('0.2')
>>> x+y
Decimal('0.3')
>>> print(x+y)
0.3
>>> print(1+x)
1.1
>>> print(1.1+x)
enter 1st number: 
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#25>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'float' and 'decimal.Decimal'
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(1.1+x)
TypeError: unsupported operand type(s) for +: 'float' and 'decimal.Decimal'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/apport_python_hook.py", line 72, in apport_excepthook
    from apport.fileutils import likely_packaged, get_recent_crashes
  File "/usr/lib/python3/dist-packages/apport/__init__.py", line 5, in <module>
    from apport.report import Report
  File "/usr/lib/python3/dist-packages/apport/report.py", line 15, in <module>
    import xml.dom, xml.dom.minidom
  File "/usr/lib/python3.8/xml/dom/minidom.py", line 23, in <module>
    from xml.dom.xmlbuilder import DOMImplementationLS, DocumentLS
  File "/usr/lib/python3.8/xml/dom/xmlbuilder.py", line 3, in <module>
    import copy
  File "/home/student/copy.py", line 1, in <module>
    n1=int(input("enter 1st number: "))
ValueError: invalid literal for int() with base 10: ''
>>> for x in range(10):
	print(i, end=' ')
	if x==6:
		break

	
1 1 1 1 1 1 1 
>>>  for x in range(10):
	print(x, end=' ')
	if x==6:
		break
	
SyntaxError: unexpected indent
>>> 
>>> for x in range(10):
	print(x, end=' ')
	if x==6:
		break

	
0 1 2 3 4 5 6 
>>> (1==2) and (2==2)
False
>>> import statistics
>>> m=statistics.mean([1,1.4,3,9,7,8,9,4])
>>> m
5.3
>>> L = [1,1,1,3,2,2,5,2,7]
>>> import Statistics as s
enter 1st number: 
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#40>", line 1, in <module>
ModuleNotFoundError: No module named 'Statistics'
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    import Statistics as s
ModuleNotFoundError: No module named 'Statistics'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/apport_python_hook.py", line 72, in apport_excepthook
    from apport.fileutils import likely_packaged, get_recent_crashes
  File "/usr/lib/python3/dist-packages/apport/__init__.py", line 5, in <module>
    from apport.report import Report
  File "/usr/lib/python3/dist-packages/apport/report.py", line 15, in <module>
    import xml.dom, xml.dom.minidom
  File "/usr/lib/python3.8/xml/dom/minidom.py", line 23, in <module>
    from xml.dom.xmlbuilder import DOMImplementationLS, DocumentLS
  File "/usr/lib/python3.8/xml/dom/xmlbuilder.py", line 3, in <module>
    import copy
  File "/home/student/copy.py", line 1, in <module>
    n1=int(input("enter 1st number: "))
ValueError: invalid literal for int() with base 10: ''
>>> import statistics as s
>>> mode_=s.mode(L)
>>> mode_
1
>>> for row in range(10):
	for column in range(10):
		print('<' if roe%2==1 else '>', end=' ')
		print()

		
enter 1st number: 
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#48>", line 3, in <module>
NameError: name 'roe' is not defined
Traceback (most recent call last):
  File "<pyshell#48>", line 3, in <module>
    print('<' if roe%2==1 else '>', end=' ')
NameError: name 'roe' is not defined

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/apport_python_hook.py", line 72, in apport_excepthook
    from apport.fileutils import likely_packaged, get_recent_crashes
  File "/usr/lib/python3/dist-packages/apport/__init__.py", line 5, in <module>
    from apport.report import Report
  File "/usr/lib/python3/dist-packages/apport/report.py", line 15, in <module>
    import xml.dom, xml.dom.minidom
  File "/usr/lib/python3.8/xml/dom/minidom.py", line 23, in <module>
    from xml.dom.xmlbuilder import DOMImplementationLS, DocumentLS
  File "/usr/lib/python3.8/xml/dom/xmlbuilder.py", line 3, in <module>
    import copy
  File "/home/student/copy.py", line 1, in <module>
    n1=int(input("enter 1st number: "))
ValueError: invalid literal for int() with base 10: ''
>>> for row in range(10):
	for column in range(10):
		print('<' if roe%2==1 else '>', end=' ')
	print()

	
enter 1st number: 2
enter 1st number: 3
enter 1st number: 3
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#50>", line 3, in <module>
NameError: name 'roe' is not defined
3Traceback (most recent call last):
  File "<pyshell#50>", line 3, in <module>
    print('<' if roe%2==1 else '>', end=' ')
NameError: name 'roe' is not defined

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/apport_python_hook.py", line 72, in apport_excepthook
    from apport.fileutils import likely_packaged, get_recent_crashes
  File "/usr/lib/python3/dist-packages/apport/__init__.py", line 5, in <module>
    from apport.report import Report
  File "/usr/lib/python3/dist-packages/apport/report.py", line 15, in <module>
    import xml.dom, xml.dom.minidom
  File "/usr/lib/python3.8/xml/dom/minidom.py", line 23, in <module>
    from xml.dom.xmlbuilder import DOMImplementationLS, DocumentLS
  File "/usr/lib/python3.8/xml/dom/xmlbuilder.py", line 3, in <module>
    import copy
  File "/home/student/copy.py", line 4, in <module>
    sum_= sum(n1+n2+n3)
TypeError: 'int' object is not iterable

>>> for row in range(10):
	for column in range(10):
		print('<' if row%2==1 else '>', end=' ')
		print()

		
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
< 
< 
< 
< 
< 
< 
< 
< 
< 
< 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
< 
< 
< 
< 
< 
< 
< 
< 
< 
< 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
< 
< 
< 
< 
< 
< 
< 
< 
< 
< 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
< 
< 
< 
< 
< 
< 
< 
< 
< 
< 
> 
> 
> 
> 
> 
> 
> 
> 
> 
> 
< 
< 
< 
< 
< 
< 
< 
< 
< 
< 
>>> 