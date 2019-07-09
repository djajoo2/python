Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # relational operator
>>> 3>5
False
>>> 4>=5
False
>>> # we convert true or false into int
>>> x=True
>>> y=int(x)
>>> y=1
>>> 
>>> 
>>> y
1
>>> x=True
>>> y=int(x)
>>> y
1
>>> int(False)
0
>>> bool(4)
True
>>> bool(1)
True
>>> bool(0)
False
>>> 
>>> 
>>> "abc"=="def"
False
>>> "ab"<"cd"
True
>>> "ab"=="ab"
True
>>> 3+4j++2+4j
(5+8j)
>>> 3+4j==4+2j
False
>>> 3+4j>2+5j
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    3+4j>2+5j
TypeError: '>' not supported between instances of 'complex' and 'complex'
>>> # note
>>> True+5
6
>>> True+3.5
4.5
>>> 
>>> 5>4>3
True
>>> 5>4>3>2<1
False
>>> "ab">1
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    "ab">1
TypeError: '>' not supported between instances of 'str' and 'int'
>>> 2+4j==2+4j
True
>>> 5=="5"
False
>>> "a"==97
False
>>> ord('a')==97
True
>>> # note exception case
>>> 5==5.0
True
>>> True==1
True
>>> False==0
True
>>> True<5
True
>>> 6<50.0
True
>>> true!=False
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    true!=False
NameError: name 'true' is not defined
>>> True!=False
True
>>> 
