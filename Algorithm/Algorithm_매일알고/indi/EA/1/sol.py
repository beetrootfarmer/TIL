def solution(speed_limit, camera):
    answer = 0                     #  과속 한 횟수를 리턴
                                    # camera에는 카메라 위치, 자동차가 통과한 시각이 담겨있음
    time = 0                        # 지금 시간
    dis = 0                         # 지금 위
    for cam, hour in camera:
        h = hour - time             # 걸린 시간
        km = cam - dis               # 이동 거리
        kmh = km / h               # 평균 속도
        if kmh > speed_limit:
            answer += 1
        time, dis = hour, cam       # 앞전 시간, 위치로 갱신
    return answer


res = solution(30, [[60,3], [152,6], [240, 9]])
print(res)