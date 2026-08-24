def solution(sequence, k):
    left = 0
    right = 0
    min_length = float('inf')
    answer = []
    current_sum = sequence[0]
    
    while right < len(sequence):
        if current_sum < k:
            right += 1
            if right < len(sequence):
                current_sum += sequence[right]
        elif current_sum > k:
            current_sum -= sequence[left]
            left += 1
        else :
            length = right - left
            if length < min_length:
                min_length = length
                answer = [left, right]
            current_sum -= sequence[left]
            left += 1   
    return answer