our_list=[12,13,-34,56,34]
print(our_list)
print(type(our_list))
jackson=["A","B","c","D",1,2,3,"Do","Puyi",True,False]
print(jackson[4])
print(jackson[9])
print(jackson[7])
print(jackson[-7])
k=jackson[2]
print(k)
# to get multiple items we do slicing
# i.e - jackson[start:end:step ]
print(jackson[0:10:3])
print(jackson)


our_list=[1,2,[3,46,56,34],454,65,767]
print(our_list)
print(our_list[1])
print(our_list[2])
print(our_list[2][0])
print(our_list[2][3])
print(our_list[2][0:])
print(our_list[2][1:])
print(our_list[2][:2])
print(our_list[2][0::2])
print(our_list[2][0::3])

#creating tables
our_tables=[[1,3,44,34],[43,5,6,887,56],[23,45,65,78],[34,34,546,786],["a","1"]]
print(our_tables)
print(our_tables[0])
print(our_tables[3])
print(our_tables[2])
print(our_tables[2][2])


#to create matrix table of order 3*3
my_table=[[1,2,3],[4,5,6],[7,8,9]]
print(my_table[0])
print(my_table[1])
print(my_table[2])
# to get elements of row and columns
print(my_table[0][0])
print(my_table[0][1])
print(my_table[0][2])

print(my_table[1][0])
print(my_table[2][2])

print(my_table[0][0:2])
print(my_table[2][1:])