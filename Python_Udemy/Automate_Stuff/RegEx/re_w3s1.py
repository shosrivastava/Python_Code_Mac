#Check if the string 
#starts with "The" and ends with "Spain"

import re

txt = 'The rain in Spain.'

pattern = re.search('^The.*Spain.$', txt)

if pattern:
    print("A match has been found.\n")
    print(pattern.group())
else:
    print("No match was found.\n")