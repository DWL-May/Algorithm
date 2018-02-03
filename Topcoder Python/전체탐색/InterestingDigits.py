base = 9
digits = []
for i in range(2,1000):
    digits.append(i)
    for j in range (i,1000,i):
        num = j
        result = 0
        while num >= 1:
            result += int(num % base)
            num = int(num / base)
        if result % i != 0:
            print(digits)
            digits.pop()
            break

print(digits)

