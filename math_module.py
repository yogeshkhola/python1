Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> round(2.4)
2
>>> round2.5)
SyntaxError: invalid syntax
>>> round(2.5)
2
>>> round(1.5)
2
>>> round(3.5)
4
>>> round(2.5)
2
>>> round(4.5)
4
>>> import mat
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    import mat
ModuleNotFoundError: No module named 'mat'
>>> sin(30)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    sin(30)
NameError: name 'sin' is not defined
>>> import math
>>> sin(30)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sin(30)
NameError: name 'sin' is not defined
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> math.sin(30)
-0.9880316240928618
>>> math.sin(0)
0.0
>>> math.floor(2.7)
2
>>> math.ceil(3.4)
4
>>> math.upper(4.5)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    math.upper(4.5)
AttributeError: module 'math' has no attribute 'upper'
>>> math.sin(pi)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    math.sin(pi)
NameError: name 'pi' is not defined
>>> math.sin(math.pi)
1.2246467991473532e-16
>>> math.sin(45)
0.8509035245341184
>>> math.sin(60)
-0.3048106211022167
>>> math.sin(math.pi/2)
1.0
>>> math.floor(math.sin(math.pi))
0
>>> math.cos(0)
1.0
>>> math.cos(math.pi)
-1.0
>>> math.asin(0)
0.0
>>> math.asin(math.pi/6)
0.5510695830994463
>>> math.sin(math.pi/6)
0.49999999999999994
>>> math.hypot(3,4)
5.0
>>> math.pow(4,3)
64.0
>>> math.exp(3)
20.085536923187668
>>> math.log(1)
0.0
>>> math.log(math.exp)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    math.log(math.exp)
TypeError: must be real number, not builtin_function_or_method
>>> math.log(math.e)
1.0
>>> math.log8(64)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    math.log8(64)
AttributeError: module 'math' has no attribute 'log8'
>>> math.log2(8)
3.0
>>> math.log10(10000)
4.0
>>> math.log3(27)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    math.log3(27)
AttributeError: module 'math' has no attribute 'log3'
>>> 