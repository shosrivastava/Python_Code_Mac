
#Return a list containing every occurrence of "ai":
import re

txt = 'The rain in Spain'

pattern = re.compile('ai')

match = pattern.findall(txt)

print(match)