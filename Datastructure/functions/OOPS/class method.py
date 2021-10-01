import random

class Pound:
    
    # def __init__(self):

        # this is the way to define a constructer 
        # this is a function ..self as a parameter 
        # self is an isinstance 

        # constructer can have more than one parameter 
    def __init__(self,rare=False):
        # rare is False by default 

        self.rare=rare

        if self.rare: #means True
            self.value=1.25
        else:
            self.value=3.00    

    

        # self.value=1.00
        self.colour="gold"
        self.num_edges=1
        self.diameter=22.5
        self.thickness=3.15
        self.head=True

    def __del__(self):
        print("coin spent!")    


# coin1=Pound(rare=True)
# print(coin1.value)

# coin2=Pound()
# print(coin1.rare)
# print(coin2.rare)

# print(coin1.value)
# print(coin2.value)
    
    # create a rust method...after rust..color change gold to greenish

    def rust(self):
        self.colour="greenish"



    def flip(self):
        heads_options=[True,False]
        choice=random.choice(heads_options)
        self.heads=choice

# coin1=Pound()        
# coin2=Pound()        
# print(coin1.colour)
# print(coin2.colour)

# coin1.rust()
# print(coin1.colour)
# print(coin2.colour)

# coin1=Pound(rare=True)
# coin2=Pound()
# print(coin1.rare)
# print(coin2.rare)
   

#  function to clean the roast 
   
#     def clean(self):
#         self.colour="gold"

# coin1=Pound()
# coin1.rust()
# print(coin1.colour)

# coin1.clean()
# print(coin1.colour)

# to make coin flip randomly...
# we import random library
    

    # def flip(self):
    #     heads_options=[True,False]
    #     choice=random.choice(heads_options)
    #     self.heads=choice

# coin1=Pound()
# print(coin1.heads)

coin1=Pound()
# coin1.flip()
# print(coin1.heads)
# print(coin1.flip)

del coin1
# print(del 
# decoin1)
del coin1

