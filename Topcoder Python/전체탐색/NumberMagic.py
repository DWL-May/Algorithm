def theNumber(answer):
    A = [1,2,3,4,5,6,7,8]
    B = [1,2,3,4,9,10,11,12]
    C = [1,2,5,6,9,10,13,14]
    D = [1,3,5,7,9,11,13,15]

    for i in range(16):
        if check(A, i) != answer[0]:
            continue
        if check(B, i) != answer[1]:
            continue
        if check(C, i) != answer[2]:
            continue
        if check(D, i) != answer[3]:
            continue

        return i
    return 0

def check(X, number):

    for x in X:
        if x == number:
            return "Y"

    return "N"

print(theNumber("YNNN"))