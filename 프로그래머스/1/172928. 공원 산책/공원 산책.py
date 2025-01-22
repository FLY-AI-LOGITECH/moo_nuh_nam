def solution(park, routes):
    answer = []
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                sc, sr = i, j  
                break

    for i in range(len(routes)):
        count = 0  
        direction = routes[i][0] 
        count = int(routes[i][2])  
        rc, rr = sc, sr  

        for k in range(count):
            if direction == 'E': 
                sr += 1
            elif direction == 'W':  
                sr -= 1
            elif direction == 'S':  
                sc += 1
            elif direction == 'N':  
                sc -= 1

            if sc < 0 or sc >= len(park) or sr < 0 or sr >= len(park[0]) or park[sc][sr] == 'X':
                sc, sr = rc, rr
                break

    return [sc, sr]