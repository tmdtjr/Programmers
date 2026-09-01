def solution(s):
    
    numbers = [int(x) for x in s.split()]
    largest = max(numbers)
    smallest = min(numbers)
    
    answer = str(smallest) + " "+ str(largest)
    
    return answer
    
        

    