# we learn tricks related to function 

# UNPACKED ARGUMENTS 
from os import name


# print(1,2,3,4,5)

numbers=[1,2,3,4,5]
# this whole is one argument
print(numbers)
 #this |(list)is packed arguments 
   
#  to unpacked it  
print(*numbers)
# five  mini arguments  
# it take each item from iterable datatype(list or string) and each those ites becomes it's own arguments to the fruntion

print("abc")
print(*"abc")
# the above is same as the  lower it unpacked each individual item
print("a","b","c")

# how to pack argumetns 

def add(x,y):
    return x+y

print(add(2,3))    
# here we can give only two values 

# to pack in many no. as possible 
def add(*numbers):
    # it takes the all values and store in a touple 
    total=0
    for number in numbers:
        total=total+number
    return total

print(add(1,2,3,4,5,6,7,8,9,10))
# all these are stored in touple and we loop through that and return that value  

def about(name,age,likes):
    sentence="Meet {}! They are {} years old and they like {}".format(name,age,likes)
    return sentence

# print(about("yogesh",22,"python"))

# dictionary={"name":"Ziyad","age":22,"likes":"Python"}

# dictionary={"age":33,"name":"yogesh","likes":"sapna"}

# print(about(**dictionary))
# we use one* for normal arguments and two * for keyword argument 

print(about(name="yhkjh",age=43,likes="dfg"))


# TO USE function WITHOUT DEFINING PARAMETERS  
# USE KWARGS AND ARGS 

def foo(**kwargs):
    for key,value in kwargs.items():
        # it gives dictioonaryu as output 
        print("{}:{}".format(key,value))


foo(khola="male",kjk="rgf",tytg="yfy",fyjf="giug")   

# these are the ways to to pack items 
