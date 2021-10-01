# classes and objects 
# clases are templated to make objects  

# making a coin object  using a class 


from os import path


class Pound:
    # we have six states to define our class 
    # object is an isinstance of class 

    value=1.00
    colour="gold"
    num_edges=1
    diameter=22.5 #mm
    thickness=3.15
    
    heads=True


coin1=Pound()
# means coin 1 have class Pound...and it has all the properties of class Pound which we define in it 

print(type(coin1))
print(coin1.value)
print(coin1.thickness)
print(coin1.colour)

# to change the value of the class
coin1.colour="greenish"
print(coin1.colour)

 
coin2=Pound()
print(coin2.colour)
# we get the colour of coin2 gold that is which we define in hte value of the class..
# this is the difference between object and classes 

# classes are the base templets...the all new objects made from...once object is made each obj has unique chracter and independent on others...
# object behave independently each other 
