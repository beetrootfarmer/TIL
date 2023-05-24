def solution(num):
    answer = 0
    for i in range(1,num+1):
        strnum = str(i)
        if '3' in strnum:
            answer += 1
        elif '6' in strnum:
            answer += 1
        elif '9' in strnum:
            answer += 1

    return answer

res = solution(33)
print(res)