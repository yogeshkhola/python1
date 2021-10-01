#touples are immutable datatypes
from io import BufferedReader
from typing import Iterable


our_touple=1,2,3,"A","B","c"
print(type(our_touple))
# we bound touple inn paranthesis
# print(type(our_touple=(1,2,3,"A","B","c")))
# print(type(our_touple))
our_touple=(1,2,3,"A","B","c")
print(type(our_touple))

# they are Iterable datatyppes  means we cann operate slicing and manyu more function on it 
print(our_touple[0:3])

# only differance with list is that touples are immutable  


list=[1,3,4,"a","e","i"]
list[2]=12
print(list)
# now chk inhn case of touples
our_touple=1,2,3,"A","B","c"
print(our_touple[2])
# our_touple[2]=34
print(our_touple)
# we get the error that touple object not suportee dthe item assignmet

# chk in case of string 
# string is also immutable 

s="1234556"
# s[2]="3"
print(s)
print(type(s))

#list are mutable...while touples and strngs are immutable  can't be changed
# we can chnage other data tye in touple 
A=[1,2,3]
print(A)
print(type(A))
A=tuple(A)
print(A)
print(type(A))
# we can assign multiple values with touples
(A,B,C)=1,2,3
print(A) 
print(B)
print(B)
print(C)
# we can do the same with list and string 
# [D,E,F]-1,2,3
# print(F)

G,H,I="789"
print(G)

P,Q,R=[9,11,3]
print(P)

