my_dict = {
    "Male" : ["Shobhit", "Sam", "Terren", "Lokesh"],
    "Female": ["Samantha", "Jessica", "Rosy", "Fiama"]
}

for i in my_dict.keys():
    for j in my_dict[i]:
        if "S" in j:
            print(j)