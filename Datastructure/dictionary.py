# we use curly brackets in dictionary 
# keys and values seperated by :
# key must be string 

from typing import List


students={"Harry":25,"Larry":23,"Yogesh":22,"Sapna":21}
# print(type(students))  
print(students["Harry"])  
print(students)
students["Harry"]=234
# dict is mutable datatypes 
print(students)
# to add a key and value in dict 
students["Fred"]=25
print(students)

# to remove
del students["Fred"]
print(students)

print(students.keys()) 
print(students.values())

# dictionary is iterable datatypes 
# BUT DOESN'T SUUPORT INDEXING 
# print(students.keys()[1])
# to access idexing change dict into list 
a=list(students.keys())
print(a)
print(a[0])
print(a[3])

# DICTIONARY DOESN'T HAVE ORDER ONLY WAY TO ITERABLE IT USE KEY 
# print(list(students.values()))[2:]
print(students)
print(students)



# to get the list of touples 
print(students.items())