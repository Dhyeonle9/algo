def solution(s):
    answer = True
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
            
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                answer = True
            else:
                return False
        
    if stack:
        return False

    return answer