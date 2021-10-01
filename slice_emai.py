#get user email address
email=input("What is your name?: ").strip()
#it striip all blank spaces

#slice out user name
# i.e yogeshkhola1520@gmail.com

user=email[:email.index("@")]

#slice domain name
#slice after @ symbol

domain=email[email.index("a")+1:]


#format message

output="Your username is {} and your domain name is{}".format(user,domain)
#display output message
print(output)
