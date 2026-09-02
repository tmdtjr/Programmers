def solution(s):
    words = s.split(' ')
    answer = []
    
    for word in words:
        if word == "":
            answer.append(word)
        else:
            new_word = word[0].upper() + word[1:].lower()
            answer.append(new_word)
        
    return " ".join(answer)