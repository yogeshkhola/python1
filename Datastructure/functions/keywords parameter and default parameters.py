
#  to make function much more flexible 

def  about(name,age,likes):
    sentence="Meet {} They are {} years old  and they like {}".format(name,age,likes)
    return  sentence
    # print(sentence)




# about("Yogesh",32, "Pyhton") 
# /*this can't woek as we use return keyword*/
print(about("Yogesh", 288, "Pyhton"))
# this is POSITON ARGUMETNS as we write in specific order  

# print(about("Yogesh  , Sapna", 22, "Pyhton"))


# here we can seethe difference betewwen parameters and argumetns  

# parameters are those which we use in function defination i.e name,age,likes
# argument are those which we pass/gives to the function when we call them i.e jack,23,pythoin
# aruments must be in specific ordrer or we can do the other way like this by giving the value to the keywords

print(about(age=23,name="khola sapna",likes="java"))
# this is KEYWORD ARGUMENT  

# these are keyword argumets each argumetns associted with keywords which matches the paramets in function defnation 


# another way to call fucnton with paramete is giving them default value when we define the functionn  

# print(about("Yogesh", 22, ))  this will not work as one argumet is missing 
# to call the funcion by two arguments we use default value 

# def  about(name="pk",age,likes="C++"):
def  about(name="sapna",age=22,likes="C+++"):


    # default parameter at last  
    sentence="Meet {} They are {} years old  and they like {}".format(name,age,likes)
    return  sentence

print(about("Yogesh", 22 )) 
print(about())
# now this works properly as we give default value of likes in function defination (parameters )

# default parameters must go at the end when we write them in fuunvtion defination 
# they can be overwrite 
# print(about("Yogesh", 22 ,"Football")) 

# print(about(23))
# non-default argument follows default argument


# print(about("ho",9 ))

# if we give default value all them    
# default value work when not give value /arguments to the fuinctuojn


def about(name="Sapna",age=22,like="Yogesh"):
    sent="Hey! my name is {},I am {} and love {}".format(name,age,like)
    return sent

print(about("Yogesh",22,"Sapna"))
# print(about())
print(about())