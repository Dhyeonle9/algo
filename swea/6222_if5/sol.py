import sys

sys.stdin = open('input.txt')

char = input()

# if char.islower:
#     print(f'{char}(ASCII: {ord(char)}) => {char.upper()}(ASCII: {ord(char.upper())})')
# elif char.isupper:
#     print(f'{char}(ASCII: {ord(char)}) => {char.lower()}(ASCII: {ord(char.lower())})')
# else:
#     print(char)

if char.islower():
    result = char.upper()

else:
    result = char.lower()

print(f'{char}(ASCII: {ord(char)}) => {result}(ASCII: {ord(result)})')
