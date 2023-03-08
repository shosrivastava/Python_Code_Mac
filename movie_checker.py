print("This code checks the movie and it's ticket for viewing.\n")

movies_available = {"Finding Nemo": [5, 1],
                    "Bourne": [12, 5],
                    "Top Gun": [15, 5]}

while True:
    choice = input("Enter youyr choice for the movie:\n").strip().title()

    if choice in movies_available:
        age = int(input("Enter your age:\n").strip())

        if age >= movies_available[choice][0]:

            if movies_available[choice][1] > 0:
                print("Enjoy the film.\n")

                movies_available[choice][1] = movies_available[choice][1] - 1

            else:
                print("Sorry, all the tickets are sold out!\n")
        else:
            print("You are too young to watch this movie.\n")

    else:
        print("Sorry, the movie entered by you is not available!\n")
        