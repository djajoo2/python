Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # logical opertor
>>> 3>4 and 5<4
False
>>> 3!=4 and 10<20
True
>>> 4>3 and 3<2
False
>>> 
>>> #note
>>> 5 and 4
4
>>> 0 and 4
0
>>> 3 and 5
5
>>> 3 and 3.5
3.5
>>> 3 and "ab"
'ab'
>>> 3 or 4
3
>>> # note in boolean for "and" if first is false then result is x otherwise second one
>>> # in "or" if first is false then result is secod one otherwise first
>>> 0 or 5
5
>>> 0 or False
False
>>> 3 or False
3
>>> 
>>> 
>>> 
>>> # not operator
>>> not 4>3
False
>>> not 5
False
>>> not 3
False
>>> 4j
4j
>>> not 3+4j
False
>>> not 0+0j
True
>>> not "saurabh"
False
>>> not ""
True
>>> "ram" and "shyam"
'shyam'
>>> "ram" or "shyam"
'ram'
>>> 3 and 4>2
True
>>> 3 and 3+4
7
>>> 3 and x==4
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    3 and x==4
NameError: name 'x' is not defined
>>> # note
>>> 3 or 5/0
3
>>> 3 and 5/0
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    3 and 5/0
ZeroDivisionError: division by zero
>>> 
