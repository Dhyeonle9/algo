import sys

while True :
    line = sys.stdin.readline().rstrip('\n')

    if not line:
        break
    
    
    lower , upper, num, blank = 0,0,0,0
    for i in range(len(line)) :
            if line[i] == " " :
                blank += 1
            elif line[i].isupper() :
                upper += 1
            elif line[i].islower() :
                lower += 1
            else :
                num += 1
    print(lower,upper,num,blank)
