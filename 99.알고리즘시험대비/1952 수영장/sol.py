# 혜지
# 한시간만에 풀어서 이게 뭔가 했는데
# 49/50 개 통과..
import sys
sys.stdin = open('input.txt')

def for_month(day, month):
    result = [0 for _ in range(12)]
    for i in range(12):
        d = plans[i] * day
        result[i] = d if d < month else month
    return result

def for_three_months(mon3):
    global monthly
    # 3개월권만 혹은 3개월권과 월권일권을 섞어 사용한 경우중 가장 적은 금액이 필요한 경우를 리턴할 result
    # 일일권으로만 했을떄 금액과 비교 계속 비교
    summon = sum(monthly)
    result = summon

    # (1월 ~ 11월 부터 3개월권을 사용했을 때) * (3개월권을 1~4번 썼을 때의 경우)
    for m in range(11):
        # 한번 썼을 때 mon3 + sum(monthly[m:m+3])
        used_one_mon3 = mon3 + (summon - sum(monthly[m:m+3]))
        if used_one_mon3 < result:
            result = used_one_mon3
        # 지금 위치에서부터 3개월권 쓰는게 더 비싸면 탐색을 멈춰
        else:
            continue
        # 지금 3개월권 쓰고 이후 자리도 3개월권으로 바꿔서 비교해봐야지
        for m2 in range(m+3, 11):
            used_twice_mon3 = mon3 + used_one_mon3 - sum(monthly[m2:m2+3])
            if used_twice_mon3 < result :
                result = used_twice_mon3
            else:
                continue
            for m3 in range(m2+3, 11):
                used_fourth_mon3 = mon3 + used_twice_mon3 - sum(monthly[m3:m3+3])
                if used_fourth_mon3 < result:
                    result = used_fourth_mon3
    if mon3*4 < result:
        result = mon3*4
    return result



T = int(input())
for tc in range(1, T+1):
    # 기간 별 가격
    day, month, months3, year = map(int, input().split())
    # prices = list(map(int, input().split()))
    # 어떻게 입력받는게 나을지..?

    # 1년간 이용계획
    plans = list(map(int, input().split()))

    # 다양한 이용 계획에 대해 가격을 도출해서 비교
    # 1) 개월별로 이용할 떄 가장 작은 경우(1개월권 혹은 1일권)의 합
    # 2) 3개월권을 이용했을 떄 모든 경우의 수
    # 3) 위에서 도출된 비용이 1년권과 비교했을 떄 더 저렴한지?

    # 1)
    monthly = for_month(day, month)
    # 2)
    result = for_three_months(months3)
    # 3)
    if year < result:
        result = year
    print(f'#{tc} {result}')

    #================ 통과 못한 테케 뭘까 죽여버려...다른사람 코드 참고해서 통과함
    # ================ 근데 원래 코드에서 뭐가 잘못됐는지 찾기보다
    # 더 완전하게 탐색하는 방법이 뭘지 고민하는게 맞는거다
    # ㅠㅠ
    # 아래는 수정한 코드
    # 혜지
    T = int(input())
    for tc in range(1, T + 1):
        # 기간 별 가격
        day, month, months3, year = map(int, input().split())
        # prices = list(map(int, input().split()))
        # 어떻게 입력받는게 나을지..?

        # 1년간 이용계획
        plans = [0] + list(map(int, input().split()))
        result = [0 for _ in range(13)]

        # 다양한 이용 계획에 대해 가격을 도출해서 비교
        # 1) 개월별로 이용할 떄 가장 작은 경우(1개월권 혹은 1일권)의 합
        # 2) 3개월권을 이용했을 떄 모든 경우의 수
        # 3) 위에서 도출된 비용이 1년권과 비교했을 떄 더 저렴한지?

        # 1)
        for i in rang e(1, 13):
            result[i] = min(plans[i] * day, month) + result[i - 1]
        # 2)
            if i > 2:
                result[i] = min(result[i], months3 + result[i - 3])
        # 3)
        print(f'#{tc} {min(year, result[12])}')