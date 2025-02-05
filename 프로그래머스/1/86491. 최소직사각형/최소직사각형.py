def solution(sizes):
    answer = 0
    for i in sizes:
        i.sort()
    max1=i[0]
    max2=i[1]
    print(type(max1))
    for i in sizes:
        if i[0] > max1:
            max1 = i[0]  
        if i[1] > max2:
            max2 = i[1]  
    answer = max1*max2
    return answer