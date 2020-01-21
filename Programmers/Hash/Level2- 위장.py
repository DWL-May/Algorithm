def solution(clothes):
    answer = 1
    a = {}
    for pair in clothes :
        if  pair[1] in a :
            a[pair[1]] += 1
        else:
            a[pair[1]] = 1
            
    for num in a.values():
        answer *= (num + 1)
        
    return answer - 1