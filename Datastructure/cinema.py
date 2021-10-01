# first elemment is age and 2nd is seats 
films={
    "Finding Dory":[3,5],
    "Tarzen":[18,5],
    "Bhaubali":[20,2],
    "Krish 3":[18,6]
}

# to maintain the infinite loop 
while True:
    choice=input("Which movie would you like to watch? :").strip().title()

    if choice in films:
        # pass
        # chk users age 
        age=int(input("How old are you? :").strip())

        if age >= films[choice][0]:
            # chk enough seats

            num_seats=films[choice][1]
            if num_seats > 0:

            # if films[choice][1>0]:

                print("Enjoy the show")
                # num_seats
                films[choice][1]=films[choice][1]-1

            else:`
            `

               print("sry we are sold out")        






        else:
            print("Baap ko bhej tere bski nhi")    
    else:
        print("Sorry this movie isn't listed in our show")