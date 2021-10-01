"""
i.e  pig-> igPay
happy-appyHay
glove-oveGlay

first letter at the end with capitalize and adding ay following to it

apple=appleyay
eat-eatyay
"""

# get sentance from the user  
original=input("Enter the sentance:").lower().strip()

# split sentence into words 
words=original.split()


# split function split the words into list 
# print(words)


# loop throgh words and convert to pig latin 
new_words=[]
# if sentence starts with vowel add "yey " at the end otherwise ,move the first consonant cluser to end add "ay"

for word in words:
    # print(word)
    if word[0] in "aeiou":
        new_word=word+"yey"
        new_words.append(new_word)

    else:
        vowel_pos=0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos+=1
            else:
                break
        cons=word[:vowel_pos]        
        the_rest=word[vowel_pos:]
        new_word=the_rest+cons+"ay"
        new_words.append(new_word)


# print(new_words)        


# stick words back together 
output=" ".join(new_words)
# join the words by space 

# output the final string
print(output)