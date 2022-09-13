def solution(n, times):
    line = 0
    time = 0
    case = []
    for j in range(0,len(times)):
        if (line + (j+1) * 2) <= n:
            line += (j+1) * 2
            time += times[j]
        for i in range(0, len(times)):
            if (line == n):
                case.append(time)
                time, line = 0, 0
            elif (line + (i+1) * 2) <= n:
                line += (i+1) * 2
                time += times[i]

    case.sort()
    print(case)
    # answer = case[0]
    answer = 0
    return answer

    # line이 두 개 일때 1번 더 자르면 4개가 아니라 3개인걸 고려하지 못해서 틀림