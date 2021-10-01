Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> word="abcdefghijklmnopqrstuvwxyz"
>>> word[26]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    word[26]
IndexError: string index out of range
>>> word[25]
'z'
>>> word[-1]
'z'
>>> word[-5]
'v'
>>> word[-1:-5:1]
''
>>> word[-1:-5]
''
>>> 
>>> word[-1:]
'z'
>>> word[-1:5]
''
>>> len(word)
26
>>> woed.index("pqrst")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    woed.index("pqrst")
NameError: name 'woed' is not defined
>>> word.index("pqrst")
15
>>> word[word.index("stu"):word.index("yz")]
'stuvwx'
>>> word[0:5]
'abcde'
>>> 