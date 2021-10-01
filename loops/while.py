#code repeat over and over while cndsn is true 
# while True:
#     print("idff")

# while 3>4:
#     print("hjwe")
#     this is falwse so code not run

# while loop worksonly if the cndsn is true 
# while False:
#     print("iweif")

# to print no. 1 -10 we do..
# print(1)
# print(2)
# print(3)
# print(4)

# print(10)
# this is work but not a pythonic way to write the code 
# we use while loop for this 

"""

num=1
while num <= 50:
    # to print even no 
    # if num % 2 ==0:

    # to print odd no 
    if num % 2 !=0: 
       print(num)
    # num=num+1
    num+=1

"""

# to add elements in list 
list=[]
while len(list) < 3:
    new_name=input("Enter the name to be added in the list :").strip().capitalize()
    list.append(new_name)
print("Sorry list is full to be further added ")    
print(list)
