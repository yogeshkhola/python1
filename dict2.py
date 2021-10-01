"""
#list in dictionary
students={
    "Alice":["ID0001",26,"A"],
    "Bob":["ID0002",27,"B"],
    "Claire":["ID003",17,"C"],
    "Dan":["ID0004",21,"D"],
    "Emma":["ID0005",22,"E"]
    }
print(students["Alice"][0])
print(students["Dan"][1:])
"""
#dictionary in dictionary
students={
    "Alice":{"id":"ID0001","age":26,"grade":"A"},
    "Bob":["ID0002",27,"B"],
    "Claire":["ID003",17,"C"],
    "Dan":["ID0004",21,"D"],
    "Emma":{"id":"ID0005","age":27,"grade":"A+"}
    }
print(students["Alice"]["age"])
#similarly we can create all

print(students["Emma"]["id"],students["Emma"]["age"])
