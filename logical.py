Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #logical operators-combine the condions
>>> not True
False
>>> not False
True
>>> not 2>3
True
>>> not 5=5
SyntaxError: cannot assign to operator
>>> not 5==5
False
>>> if True
SyntaxError: invalid syntax
>>> if True:
	print("fd")

	
fd
>>> x=4
>>> y=5
>>> if not
SyntaxError: invalid syntax
>>> if not y<x:
	print("get it")

	
get it
>>> if not y<x:
	print("get it")

	
get it
>>> x=4
>>> y=4
>>> if not y<x:
	print("ioj")

	
ioj
>>> x=3
>>> y=2
>>> if not y<x:
	print("ref")

	
>>> 
>>> x=3
>>> y=2
>>> if not y<x:
	print("ref")

	
>>> 
x=3
>>> y=2
>>> if not y<x:
	print("ref")
	
SyntaxError: invalid syntax
>>> x=3
>>> y=2
>>> if not y<x:
	print("ref")
	
SyntaxError: multiple statements found while compiling a single statement
>>> # AND operator..both cnds must be true for 1
>>> 
>>> 
>>> False and True
False
>>> False and False
False
>>> True and True
True
>>> c=12
>>> d=5
>>> if c>12 and d>1:
	print("it worked")

	
>>> if c>10 and d>1:
	print("it worked")

	
it worked
>>> #both cndtn must be satisfiedif c>10 and d>1:
	print("it worked")
	
SyntaxError: unexpected indent
>>> #NAND OPERATION
>>> if not(c>12 and d>1):
	print("worked")

	
worked
>>> 
>>> 
>>> #OR OPERARTION-IF ANY ONE CNDSN IS TRYE THEN IT'S TRUE
>>> 
>>> C=5
>>> D=-1
>>> if C>1 or D>1:
	print("good")

	
good
>>> True or False
True
>>> True or True
True
>>> False or False
False
>>> 
>>> #NOR OPERATION
>>>  if not C>1 or D>1:
	print("good")
	
SyntaxError: unexpected indent
>>> if not C>1 or D>1:
	print("good")

	
>>> 
>>> if not C>100 or D>100:
	print("weer")

	
weer
>>> 

>>> c=6
>>> d=2
>>> if (c>5 and d>5) or (c>1 and d>1):
	print("ersere")

	
ersere
>>> not (False and True)
True
>>> 