import re

sentence = 'This is an abc example for particular issue.'

pattern = re.compile(r'abc')

matches = pattern.finditer(sentence)

for match in matches:
    print(match)

print(sentence[11:14])