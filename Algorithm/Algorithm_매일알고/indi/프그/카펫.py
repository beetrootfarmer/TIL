def solution(brown, yellow):
    answer = []
    if yellow <= 3:
        answer = [yellow+2, 3]
    else:
        for i in range(1,(yellow//2)+1):
            s = yellow // i
            if yellow%i == 0:
                # 약수인 경우
                # brown 확인
                if (s*2)+(i*2)+4 == brown:
                    answer = [s+2, i+2]
                    break

    return answer
solution(24,24)
solution(20404,2000000)