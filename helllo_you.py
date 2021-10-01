#Ask user for name
name=input("What  is your name? :")
#print(name)

#ask the user  for age

age=input("How old are you? :")
#print(age)          

 # print(type(age))          
#ask the user foor city
city=input("which city do you live in?:")


#ask the user what they enjoy
love=input("what do you love to doing")

#create output text
string="Your name is {} and you are {} years old . You live in {} and you love{}"
output=string.format(name,age,city,love)

#print output to screen
print (output)
