# in this we use to use of in keyword  
known_users=["Monu","Yogesh", "Khola","Yadav", "Kumar","Sonu","Sapna","Suman"]
# print(len(known_users))

while True:
    print("Hi! my name is Travis")
    name=input("What is your name?:").strip().capitalize()

    if name in known_users:
        print("Hello {}".format(name))
        std=input("Would you like to removed from the system (y/n)?: ").strip().lower()

        if std =="y":
            print(known_users)
            known_users.remove(name)
            print(known_users)
        elif std =="n":
            print("No problem, I didn't want you to leave anyway!")
    else:
        print("Hmmm I don't think I have met you yet {}".format(name))
        add_me=input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            print(known_users)
            known_users.append(name)
            print(known_users)

        elif add_me=="n" :
            print("No worries,see you around")
        
 
