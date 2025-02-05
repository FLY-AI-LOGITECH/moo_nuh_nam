def solution(s):
    answer = 0
    i = 0
    length = len(s)
    
    while i < length:
        if s[i] == '0' or s[i] == '1' or s[i] == '2' or s[i] == '3' or s[i] == '4' or s[i] == '5' or s[i] == '6' or s[i] == '7' or s[i] == '8' or s[i] == '9':
            answer *= 10
            answer += int(s[i])
            i += 1
        else:
            if s[i] == 'z' and i + 3 < length:
                answer *= 10
                i += 4
            elif s[i] == 'o' and i + 2 < length:
                answer *= 10
                answer += 1
                i += 3
            elif s[i] == 'e' and i + 4 < length:
                answer *= 10
                answer += 8
                i += 5
            elif s[i] == 'n' and i + 3 < length:
                answer *= 10
                answer += 9
                i += 4
            elif s[i] == 't' and i + 2 < length:
                if s[i+1] == 'w':
                    answer *= 10
                    answer += 2
                    i += 3
                elif i + 4 < length and s[i+1] == 'h':
                    answer *= 10
                    answer += 3
                    i += 5
            elif s[i] == 'f' and i + 2 < length:
                if s[i+1] == 'o':
                    answer *= 10
                    answer += 4
                    i += 4
                elif i + 3 < length and s[i+1] == 'i':
                    answer *= 10
                    answer += 5
                    i += 4
            elif s[i] == 's' and i + 2 < length:
                if s[i+1] == 'i':
                    answer *= 10
                    answer += 6
                    i += 3
                elif i + 4 < length and s[i+1] == 'e':
                    answer *= 10
                    answer += 7
                    i += 5

    return answer