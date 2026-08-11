def solution(n):
    answer = 0
    str_n = str(n)
    
    for i in range(len(str_n)):
        int_n = int(str_n[i])
        answer += int_n
    
    return answer
    