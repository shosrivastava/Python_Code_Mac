print("This code generates even numbers between 1 & 100 and store them in a list.\n")

even_nums = [i for i in range(1,101) if i % 2 == 0]
print(even_nums)

print("-------------------------------------------------------\n")

my_list = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

refined_list = [[w.lower(), w.upper(), len(w)] for w in my_list]

print(refined_list)