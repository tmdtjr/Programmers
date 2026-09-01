def solution(s):
    answer = True
    stack = []
    for char in s :
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    
    if len(stack) == 0:
        return answer
    else:
        answer = False
        return answer