def palindrome(s):

    add = 0
    back = 1
    temp = 0
    on = False
    for i in range(len(s)):
        if s[i] == s[len(s) - back]:
            back += 1
            on = True
            temp += 1
        else:
            add += 1
            if on:
                add += temp
                temp = 0
                on = False

    return len(s) + add





print(palindrome('abdfhdyrbdbsdfghjkllkjhgfds'))
