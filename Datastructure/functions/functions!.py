# in function we wite the code only once ...and can use it anywhere as we want 

# use def keyword to define a function 
def add(x,y):
# add is the function name ,x and y are the parameters     
    return x + y
    # to get out something from a fucntion it need return value to me 
add(7,3)    
# if we use print in place of return then the above line give output ``
print(add(7,3))
# call the functoin to get run
# print(add(5,6))
# print(add(5,98))

# the function return a value we can store that in a variabe 
# answer=add(3,34)
# print(answer)


# return value is no the same value which we print the value in the function
def add(x,y):
    print(x+y)

print(add(4,5))    

# print(answer=add(5,6))
answer=add(3,4)
print(answer)
print(type(answer))

add(67,3)
# it's  just empty bcz print just the value the screen it didn't do reqired process to store value in a varibale 
#  print doesn't return anything it just shown on sceen 


# to reverse the string 
word="pqrst"
print(word[::-1])

# done it using function 
def rev(text):
    return text[::-1]

# print(rev(gfwef))
print(rev("gfwef"))

# it reverse string list or any iterable datatypes 
print(rev([1,2,4,5]))

#  functions are pieces of reusable code  they takes inputs as parameters and store that in variable and use that where we want 
# returning value is imp if we want to use the value the fucnction return  letter
