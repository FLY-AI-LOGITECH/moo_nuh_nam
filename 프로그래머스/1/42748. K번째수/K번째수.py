def solution(array, commands):
    answer = []
    for i in commands:
        st = i[0]
        en = i[1]
        k = i[2]
        tmp=[]
        for j in range(st,en+1):
            tmp.append(array[j-1])
        tmp.sort()
        answer.append(tmp[k-1])
    return answer