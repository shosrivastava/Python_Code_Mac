import re

txt = 'The rain in Spain'

#Search for an upper case "S" character in the beginning of a word, and print its position

# \b	Returns a match where the specified characters are at the beginning or at the end of a word

x = re.search(r'\bS\w+', txt)

print(x.span())