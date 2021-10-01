students={
    "male":["Yogesh","Monu","Sonu","Manish","Sanjay"],
    "female":["Sapna","Suman","Sushma","Kavita","Kalpana"]
}

for key in students.keys():  #iterate keys
    # print(key)
    # print(students[key] )
    # print(students[key][1] )

    for name in students[key]:  #iterate lists
        if "a" in name:
            print(name)




#   we use range in for loops to iterate numbers 
# and use in to iterate lists and dictionary           