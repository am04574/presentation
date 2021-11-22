import re


# match the times in the text using character set
pattern = re.compile(r'\d\d[:]\d\d[-]\d[:]\d\d')

with open('data.txt' ,'r') as f:
    contents = f.read()

matches = pattern.finditer(contents)

for match in matches:
    print(match)


print('----------------------------------')
# match the courses in the text

pattern2 = re.compile(r'\w\w\w[-]\d\d\d[-]\d\d')

matches2 = pattern2.finditer(contents)

for match in matches2:
    print(match)

print('----------------------------------')

# match times using quantifiers

pattern3 = re.compile(r'\d+[:]\d\d[-]\d[:]\w+')

matches3 = pattern3.finditer(contents)

for match in matches3:
    print(match)

print('----------------------------------')

pattern3 = re.compile(r'\d+[:]\d\d[-]\d[:]\w+')

matches3 = pattern3.finditer(contents)

for match in matches3:
    print(match)