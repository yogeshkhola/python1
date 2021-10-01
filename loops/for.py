#  to print no. from 1 to 10 


# range function make iterable 
# range give iterablein python 3 while list in pyton 2 
# for i in range(10):
"""
for i in range(1,11):
    # index start from 0 
    print(i)

# we can use for loop in any case as following -list /string    
for num in [1,2,3,4]:
    print(num)

for letter in "A,B,C":
    print(letter)

for p in range(2,101,2):
    print(p)

"""
# program to find the vowels and consonents in a word
vowels=0
consonants=0
p=input("enter the letter:")
for letter in p:
    if letter.lower() in "aeiou":

        vowels+=1
    # elif letter == " ":
        # pass
    else:
        consonants+=1
# print("There are {} vowels".format(vowels)) 
# print("There are {} consonants".format(consonants))


print("There are {} vowels and {} consonants in the word ",p.format(vowels,consonants))