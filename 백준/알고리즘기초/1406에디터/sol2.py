import sys 
sys.stdin = open('input.txt')

strlist = sys.stdin.readline()
n = int(sys.stdin.readline())
location = len(strlist)
print(strlist, n, location)
for _ in range(n):
    print(location)
    command = sys.stdin.readline().split()
    print(command)
    if command[0] == 'P':
        strlist = strlist[:location] + command[-1] + strlist[location:]
    elif command[0] == 'L' and location != len(strlist):
        location -= 1
    elif command[0] == 'D' and location != 0:
        location += 1
    elif command[0] == 'B':
        strlist = strlist[:location] + strlist[location+1:]
    
print(strlist)