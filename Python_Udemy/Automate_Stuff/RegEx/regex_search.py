import re

txt = 'The rain in Spain'

pattern = re.search("\s", txt)

print(f"The first space sequence is at {pattern.start()}")