# The sub() function replaces the matches with the text of your choice:

import re

txt = 'The rain in Spain'

x = re.sub('\s', '_', txt, 2)

print('\n')
print(x)