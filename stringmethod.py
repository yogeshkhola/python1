Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> string methods
SyntaxError: invalid syntax
>>> string methods
SyntaxError: invalid syntax
>>> 4
4
>>>  #syntex :string.method()
>>> string.method()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    string.method()
NameError: name 'string' is not defined
>>> "you are the motherfucker".count(e)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    "you are the motherfucker".count(e)
NameError: name 'e' is not defined
>>> "you are the motherfucker".count("e")
4
>>> text="happy birthhday"
>>> text.count("A")
0
>>> text.count("a")
2
>>> text.count("i love you")
0
>>> text.count("happy")
1
>>> 
test="yogesh"
test.count("e")
>>> text.count("a")
2
>>> test="yogesh"
test.count("e")
>>> 
>>> pou="rikshaw"
>>> pou.count("k")
1
>>> test="yogesh"
>>> test.count("y")
1
>>> stud="Yogesh Khola"
>>> stud.upper()
'YOGESH KHOLA'
>>> stud="Yogesh Khola"
>>> stud..lower()
SyntaxError: invalid syntax
>>> stud.lower()
'yogesh khola'
>>> x
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> stud
'Yogesh Khola'
>>> #strings are immutable datatypes:unchaable
>>> x=x.lower()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    x=x.lower()
NameError: name 'x' is not defined
>>> stud=stud..lloower
SyntaxError: invalid syntax
>>> stud=stud.lower()
>>> stud
'yogesh khola'
>>> stud.upper()
'YOGESH KHOLA'
>>> stud
'yogesh khola'
>>> stud=stud.upper()
>>> stud
'YOGESH KHOLA'
>>> 

>>> #capatalisd method
>>> stud=stud.lower()
>>> stud
'yogesh khola'
>>> stud.capitalze()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    stud.capitalze()
AttributeError: 'str' object has no attribute 'capitalze'
>>> stud.capitalize()
'Yogesh khola'
>>> #capitalize the fistt lestter
>>> stud
'yogesh khola'
>>> stud.title()
'Yogesh Khola'
>>> stud
'yogesh khola'
>>> stud=stud..title()
SyntaxError: invalid syntax
>>> stud=stud.title()
>>> stud
'Yogesh Khola'
>>> #now this is overwrite
>>> stud.islower()
False
>>> stud.isupper()
False
>>> stud=stud.upper()
>>> stud
'YOGESH KHOLA'
>>> stud.isupper()
True
>>> stud.istitle()
False
>>> stud=stud.title()
>>> stud
'Yogesh Khola'
>>> stud.istitle()
True
>>> #to check everything in the varible is alphabet
>>> #to check everything in the varible is alphabet(letters)
>>> stud.isaplha()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    stud.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'
>>> stud.isalpha()
False
>>> #space is present
>>> "ahuhukewhyiuohei".isalpha()
True
>>> "12449387".isdigit()
True
>>> "ywioeuyiuoewhy987988kjhkjdf".isalnum()
True
>>> "geuigwei 868".isalnum()
False
>>> False
False
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> # .lower(),.upper(),.title(),.capitalzie(),..count(),.isalpha/digit/alnum,.isupper.islower(|)