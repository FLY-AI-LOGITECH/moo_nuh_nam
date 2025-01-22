def solution(name, yearning, photo):
    hi = dict(zip(name,yearning))
    result = []
    for i in photo:
        s=0
        for j in i:
            s+=hi.get(j,0)
        result.append(s)
    return result