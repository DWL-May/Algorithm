def theNumber(answer):
    c = [
        "YYYYYYYYNNNNNNNN",
        "YYYYNNNNYYYYNNNN",
        "YYNNYYNNYYNNYYNN",
        "YNYNYNYNYNYNYNYN"
    ]

    for i in range(16):
        temp = ""
        for j in range(len(c)):
            card = c[j]
            temp += card[i]
        if temp == answer:
            return i + 1
    return 0


print(theNumber("YNYY"))