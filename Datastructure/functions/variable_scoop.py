# global scope-if variable is in global scope , called global variable  and can be seen anywhere in the program...
# local scope- local variable and can only be seen in the specific local scope

# iin python function creates local scopes and loop, if not 

"""

a=100

def f1():
    # entering parameter are Optional 
    print(a)

def f2():
    print(a)

f1()
f2()
# print(f2())
# value printed in both is same bcz of global varaibel a 
"""

"""
# let's try another way  

def  f1():
    a=100
    print(a)

def  f2():
    print(a)

f1()
f2()

# we get output of only  first varibel ...bcz no variable is defined in fiction f2 
# varible a is in local scope of f1 and not in global scope
# so function create always local scope withinh it  
"""
"""

def  f1():
    a=100
    print(a)

def  f2():
    a=98
    print(a)

f1()
f2()

# here we get the differnt values as having teh same varibel a...bcz both haveing their own local scope varibel so they act as different 
# so we can overwrite the variable  
"""
"""
a=8768
def  f1():
    a=100
    print(a)

def  f2():
    a=98
    print(a)

f1()
f2()
print(a)

# despite having the global varibale python overwrite th local vaibel in the function if it is present with in the fiucntiomn 
# gloabl varible destroy the locals varible after the function  
"""
"""

# function first the varible within it...(local scope)..if ther no present then it looks for the global scope 

a=324
def  f1():
    # a=100
    b=a+26
    print(b)

def  f2():
    a=98
    print(a)

f1()
f2()
print(a)

# global variable not overwrite local varible inside the function
"""

"""
# global variable can be used everywehere in the program(inside the local scope) until we try to change glocal svaribel by giving value to local socpe 

# to change the global varibale inside the function we use global keywoed preceeding the varibale 

a=250
# we give gloabal varibel value 100 initially 
def  f1():
    global a
    a=87987
    # this is the wright syntex of changing global variable  
    # global a=100 is wrong 
    # here we overwrite the global variable...everywehre in the program 
    print(a)

def  f2():


    # global  a
    # if we use global here also we overwrite the value of teh global varibale again 


    a=98
    print(a)
#   inside the functionn f2  local variable overwrite the gloabl variable...
f1()
f2()

print(a)
"""

"""
# WORKING WITH LIST AND DICTIONARIES

# here changing the local varibel effect the value in the global varible value inside and outside the function as well  

# making list as global variable 
a=[1,2,3]
def  f1():
    # a=100
    # we can change a little in the global variable 
    # global a 
    # there is no need of the above code 

    
    # a[0]=87

   
    global a

    a=12

    print(a)

def  f2():
    a=98
    print(a)

f1()
f2()
print(a)

"""

# in list and dictionary make a little change in local varibale having same name of global variable change it globally 
# we not need to use keywoed global a 


a=[345,345,577]
def  f1():
    # a=100
    a[0]=900
    print(a)

def  f2():
    print(a)

f1()
f2()

print(a)