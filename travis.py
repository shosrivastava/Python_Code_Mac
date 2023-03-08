print("This code shows the TRAVIS Security System.\n")

known_users = ["Ramesh", "Mohan", "Sunny", "Lokesh"]

while True:
    print("Hello, my name is Travis.\n")
    name = input("What is your name?\n").strip().capitalize()

    if name in known_users:
        choice = input("Hello, your name is recognised. Would you like your name to be removed (y/n))?\n")

        if choice == "y":
            print(f"The original name set was {known_users}.\n")
            known_users.remove(name)
            print(f"The new name set is {known_users}.\n")

    else:
        add_name = input("Would you like your name to be added to the name set? (y or n)\n").strip().lower()
        print(f"The original name set is {known_users}.\n")
        known_users.append(name)
        print(f"The new name set is {known_users}.\n")