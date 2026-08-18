def solution(n):
    root = n ** 0.5
    if int(root) == root:
        answer = (root + 1)**2
    else:
        answer = -1
    return answer