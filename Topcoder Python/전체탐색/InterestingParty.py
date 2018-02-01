def happy_party(fisrt, second):
    dic = {}
    for i in range(len(fisrt)):
        if not fisrt[i] in dic:
            dic[fisrt[i]] = 0
        if not second[i] in dic:
            dic[second[i]] = 0

    for j in range(len(fisrt)):
        dic[fisrt[j]] += 1
        dic[second[j]] += 1
    max = 0
    print(dic)
    for friends in dic.values():
        if max < friends:
            max = friends

    return max


first = ["t", "o", "p", "c", "o", "d", "e", "r", "s", "i", "n", "g", "l", "e", "r", "o", "u", "n", "d", "m", "a", "t",
         "c", "h", "f", "o", "u", "r", "n", "i"]
second = ["n", "e", "f", "o", "u", "r", "j", "a", "n", "u", "a", "r", "y", "t", "w", "e", "n", "t", "y", "t", "w", "o",
          "s", "a", "t", "u", "r", "d", "a", "y"]
print(happy_party(first, second))
'''
    total = fisrt + second
    total = set(total)

    max = 0
    for topic in total:
        size = 0
        for i in range(len(fisrt)):
            if topic == fisrt[i] or topic == second[i]:
                size += 1
        if max < size :
            max = size

    return max

#first = ["fishing", "gardening", "swimming", "fishing"]
#second = ["hunting", "fishing", "fishing", "bitting"]

first = ["t","o","p","c","o","d","e","r","s","i","n","g","l","e","r","o","u","n","d","m","a","t"
         ,"c","h","f","o","u","r","n","i"]
second = ["n","e","f","o","u","r","j","a","n","u","a","r","y","t","w","e","n","t","y","t","w","o","s","a","t","u","r","d","a","y"]
print(happy_party(first, second))
'''
