import re

text1 = 'gfgfdAAA1234ZZZuijjkGFGend'

# literal search examples
try:
    found = re.search('AAA(.+?)ZZZ', text1).group(1)
except AttributeError:
    # AAA, ZZZ not found in the original string
    found = '' # apply your error handling
    
print(found)

# found: 1234

pattern = re.compile(r'\d\d\d')

matches = pattern.finditer(text1)
for match in matches:
    print(match)

print(text1[0:3])
print(r"\tTab")

# pattern search

# . operator matches anything except new line
# \d matches any digits between 0 and 9
# \D not a digit between 0 and 9
# \w word character : (a-z, A-Z , 0-9 or underscores _)
#  \W not word characters
# \s  whitespace (space, tabs, newlines)
# \S not a whitespace

# Anchors 
# Anchors belong to the family of regex tokens that don't match any characters, 
# but that assert something about the string or the matching process

# \b word boundary start of a line or space is one 
# \B not word boundary
#  ^ look for pattern in beginning of a string ^Start
#  $ look for at end of string

# find the g
#  ^ find Start in beginning
#  $ end 

pattern = re.compile(r'\bg')

matches2 = pattern.finditer(text1)

    
for match in matches2:
    print(match)

