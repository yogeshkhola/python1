#  short hand method to comprise loops and if to make list in one line of code

even_numbers=[x for x in range (1,101) if x%2==0]
print(even_numbers)


# keep x if it's divisible by 2  
odd_num=[p for p in range(1,101) if p%2 !=0]
# first-what the result we want to get, 2nd loop , 3rd-if there any cndsn 
print(odd_num)

# list comprenhision not only work for  numbers they work for any data types i.e strings list etc..

words=["the","quick","brown","fox","jumps","over","little","lazy", "dog"]
# another list of list 
answer=[[w.upper(),w.lower(),len(w)] for w in words]
print(answer)