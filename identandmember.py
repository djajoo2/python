Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # identity operator
>>> x=5
>>> y=5
>>> x==y
True
>>> x is y
True
>>> x=5
>>> y=6
>>> x==y
False
>>> x is y
False
>>> x=5
>>> y=5.0
>>> x==y
True
>>> x is y
False
>>> x is not y
True
>>> 
>>> 
>>> # membership operator
>>> x="abc"
>>> "a" i x
SyntaxError: invalid syntax
>>> "a" in x
True
>>> "A" not in x
True
>>> x=[10,20,30]
>>> 10 in x
True
>>> x=1,2,3,4
>>> 1 in x
True
>>> 
