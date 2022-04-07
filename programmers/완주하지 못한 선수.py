# 마라톤 참가선수와 완주한 선수 이름이 담긴 배열 두 개가 주어짐
# 완주하지 못한 선수의 이름을 출력
    # 1트
    #배열 간 빼기!
    # set 방법으로 할 경우 이름이 중복되었을 때 하나로 합쳐진다 
    
    from re import T


def solution(participant, completion):
    answer = ''
    new_list = list(set(participant) - set(completion))
    answer = new_list[0]        
    return answer

    # 2트
    # 완주자 목록에 있으면 참가자 목록에서 지우기
    # 시간초과!
    def solution(participant, completion):
    answer = ''
    for i in range(len(completion)):
        if completion[i] in participant:
            participant.remove(completion[i])
    answer = participant[0]        
    return answer

    #3트
    # 해시값 사용
    def solution(participant, completion):
    answer = ''
    notcomp = 0
    h = {}
    for p in participant:
        h[hash(p)] = participant
        notcomp += int(hash(p))
    for c in completion:
        notcomp -= hash(c)
    answer = h[notcomp]        
    return answer
    
    #다른사람 답
    #collections 사용
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]