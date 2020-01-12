def solution(participant, completion):
    answer = ''
    result = {}
    
    for p in participant :
        if p in result :
            result[p] = result[p] + 1
        else :
            result[p] = 1
        
    for c in completion :
        if c in result :
            result[c] = result[c] - 1
    
    for p in participant :
        if result[p] >= 1:
            answer = p
    return answer