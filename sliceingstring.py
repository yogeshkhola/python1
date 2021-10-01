Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> string="ahkhdkhioherghju 9478904"
>>> print(type(String))
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(type(String))
NameError: name 'String' is not defined
>>> type.string
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type.string
AttributeError: type object 'type' has no attribute 'string'
>>> print(type.string)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(type.string)
AttributeError: type object 'type' has no attribute 'string'
>>> string="uihoieojooi2309"
>>> string[0]
'u'
>>> string[87]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    string[87]
IndexError: string index out of range
>>> string[15]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    string[15]
IndexError: string index out of range
>>> string[10]
'i'
>>> print(string[0])
u
>>> #format of slice
>>> variable[start:end:step]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    variable[start:end:step]
NameError: name 'variable' is not defined
>>> string[0:5:1]
'uihoi'
>>> string[5]
'e'
>>> #e is not included string[0:5:1]
>>> string[0:5:2]
'uhi'
>>> string[5:9:1]
'eojo'
>>> string[5:10:1]
'eojoo'
>>> string[5:]
'eojooi2309'
>>> string[:9]
'uihoieojo'
>>> string[5::2]
'ejo20'
>>> #to reverese the string
>>> string[::-1]
'9032ioojoeiohiu'
>>> 