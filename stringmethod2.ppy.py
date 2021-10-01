Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x="happy birthday"
>>> x.index(birthday)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x.index(birthday)
NameError: name 'birthday' is not defined
>>> x.index("birthday")
6
>>> x.index(" ")
5
>>> x.index("  y ")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x.index("  y ")
ValueError: substring not found
>>> x.index("y")
4
>>> x.count("y")
2
>>> x.find("d")
11
>>> x.find("jioaw")
-1
>>> x.index("BIRTHDAY")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x.index("BIRTHDAY")
ValueError: substring not found
>>> x.find("BIRTHDAY")
-1
>>> y="000000000000Yogesh Khola000000000"
>>> #to remove all 0's
>>> y.strip("0")
'Yogesh Khola'
>>> z="09090090990YAdav09098")
SyntaxError: unmatched ')'
>>> z="09090090990YAdav09098"
>>> z.strip("0,9")
'YAdav09098'
>>> z.strip("0")
'9090090990YAdav09098'
>>> y="000000000000Yogesh Khola000000000"
>>> y.lstrip("0")
'Yogesh Khola000000000'
>>> y.rstrip("0")
'000000000000Yogesh Khola'
>>>  y
 
SyntaxError: unexpected indent
>>> y
'000000000000Yogesh Khola000000000'
>>> #jsut string is mutable
>>> y.strip()
'000000000000Yogesh Khola000000000'
>>> 

>>> 
>>> name=input("what is your name")
what is your namename=input("what is your name?: ")
>>> name=input("what is your name?: ")
what is your name?: Yogesh Kumar        
>>> #i use extra space after the name
>>> print(name)
Yogesh Kumar        
>>> len(name)
20
>>> name=input("what is your name?: ")
what is your name?: YK
>>> print(name)
YK
>>> len(name)
2
>>> name=input("what is your name?: ")
what is your name?: Yogesh Kumar  
>>> len(name)
14
>>> name.upper()
'YOGESH KUMAR  '
>>> name=name.upper()
>>> name
'YOGESH KUMAR  '
>>> print(name)
YOGESH KUMAR  
>>> len(name)
14
>>> #if  i use strip function it cut all unwated space
>>> name=input("what is your name?: ").strip()
what is your name?: Yogesh Khola                 
>>> name
'Yogesh Khola'
>>> print(name)
Yogesh Khola
>>> len(name)
12
>>> #lenth us redyudce that is cut down by the strip function
>>> name=kd
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    name=kd
NameError: name 'kd' is not defined
>>> name=name.upper
>>> ()name=name.upper
SyntaxError: invalid syntax
>>> name=name.upper()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    name=name.upper()
AttributeError: 'builtin_function_or_method' object has no attribute 'upper'
>>> name=name.upper()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    name=name.upper()
AttributeError: 'builtin_function_or_method' object has no attribute 'upper'
>>> name
<built-in method upper of str object at 0x000001A088D28070>
>>> name=input("what is your name?: ").strip()
what is your name?: yogesh
>>> name
'yogesh'
>>> name.upper()
'YOGESH'
>>> name=name.upper()
>>> name
'YOGESH'
>>> 