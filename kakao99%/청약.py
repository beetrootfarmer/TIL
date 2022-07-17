import operator

def solution(region, num, info):
    dic = {}
    for i in range(0, len(info)):
        score = 0
        score += (info[i][1] + 1) * 2
        score += (info[i][2] + 2)
        score += (info[i][3] + 1) * 5
        if (info[i][0] == region):
            score += 100
        dic[i] = score

    answer = [-1] * len(info)

    dic = sorted(dic.items(), key = operator.itemgetter(1), reverse=True)
    rank = 0
    for key in dic:
        for i in range(0, len(info)):
            if i in key:
                rank += 1
                answer[i] = rank
    for i in range(0, len(answer)):
        if answer[i] > num:
            answer[i] = -1
    return answer



    # 차손님 풀이
def solution(region, num, info):
    answer = [-1] * len(info)
    rank1 = []
    rank2 = []
    cnt = 0
    for i in info:
        if i[0] == region:
            rank1.append(i)
            cnt += 1
        else:
            rank2.append(i)
    rank1.sort(key=lambda i: ((i[1]+1)*2) + (i[2]+2) + (i[3]+1)*5, reverse=True)
    rank2.sort(key=lambda i: ((i[1]+1)*2) + (i[2]+2) + (i[3]+1)*5, reverse=True)

    i = 0
    j = 0
    while i < num and i < len(info):
        if i < cnt:
            answer[info.index(rank1[i])] = i + 1
        else:
            answer[info.index(rank2[j])] = i + 1
            j += 1
        i += 1
    return answer