print("This code accepts names and add them to a list.\n")

my_list = []

while len(my_list) < 3:
    name = input("Enter a name:\n").strip().capitalize()
    my_list.append(name)
print(f"The updated list with names is {my_list}.")