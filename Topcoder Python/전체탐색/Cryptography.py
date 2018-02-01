def cryptograhy (list):
    list = sorted(list)
    list[0] += 1

    result = 1
    for num in list:
        result *= num
    return result

'''
def cryptograhy (list):
    max = 0
    for i in range(len(list)):
        result = 1
        for idx , num in enumerate(list):
            if i == idx :
                num = num + 1
            result *= num

        if result > max:
            max = result

    return max
'''
#list = [1,2,3]
#list = [1,3,2,1,1,3]
list = [1000, 999, 998, 997, 996, 995]
#list = [1,1,1,1]
print(cryptograhy(list))