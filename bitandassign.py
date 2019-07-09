Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # bitwise operator
>>> 5&6
4
>>> 5|6
7
>>> 5^6
3
>>> ~5
-6
>>> 25>>2
6
>>> 12<<3
96
>>> 
>>> 
>>> # assignment operator
>>> x=1
>>> x+=3
>>> x
4
>>> x*=2
>>> x
8
>>> x/=4
>>> x
2.0
>>> x//=5
>>> 
>>> x
0.0
>>> x%=3
>>> x
0.0
>>> x&=7
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    x&=7
TypeError: unsupported operand type(s) for &=: 'float' and 'int'
>>> x*=3+4
>>> x
0.0
>>> x*=3+4
>>> x
0.0
>>> x=5
>>> x*=3+4
>>> x
35
>>> x=5
>>> x=5*3
>>> x
15
>>> x=5
>>> x=5*3+4
>>> x
19
>>> 
