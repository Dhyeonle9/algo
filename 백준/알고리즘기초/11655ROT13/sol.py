import sys

sys.stdin = open('input.txt')
w = input()
asw = ''

for i in range(len(w)):
    if w[i].isalpha():
        if (ord(w[i])>64 and ord(w[i])<78) or (ord(w[i])>96 and ord(w[i])<110):
            asw += chr(ord(w[i]) + 13)
        else:
            asw += chr(ord(w[i]) - 13)
    else:
        asw += w[i]

print(asw)