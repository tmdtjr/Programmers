def solution(n): 
    answer = []
    
    for d in str(n):
        answer.append(int(d))
    
    answer = answer[::-1]
    return answer