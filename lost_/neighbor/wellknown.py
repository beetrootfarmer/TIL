def solution(logs):
    #logs에 중복된 "이름 문제"를 제거
    setlog = set(logs)
    logs = list(setlog)

    names = [] #몇명있는지
    name_pro = []
    problem = {} #문제별로 몇명이나 풀었는지
    p = []
    for i in range(0, len(logs)):
        name_pro = logs[i].split()
        if name_pro[0] not in names:
            names.append(name_pro[0])
        if name_pro[1] not in problem:
            problem[name_pro[1]] = 1
            p.append(name_pro[1])
        else:
            problem[name_pro[1]] += 1 #문제가 중복되면 value에 +1
    half = float(len(names)) / 2
 
    for i in range (len(p)):
        if (problem[p[i]] < half):
            del problem[p[i]]
    answer = []
    for i in problem.keys():
        answer.append(i)
    return answer