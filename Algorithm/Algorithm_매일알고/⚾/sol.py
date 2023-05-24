import sys

input = sys.stdin.readline

# 이닝
N = int(input().rstrip())

# 선수들의 이닝 별 기록 리스트
# 1안타 2루타 3루타 4홈런 0아웃
records = list(list(map(int, input().split())) for _ in range(N))

# 타순
batting_order = [-1]*9
# 지정된 선수
selected = [0] * 9

# 4번타자 확정
batting_order[3] = 0
selected[0] = 1

# 현재 최고기록
best_record = 0

# 순열
seq = set()

def get_innings(order):
    global best_record

    # 모든 선수가 선택이 완료되었을 때
    # 타점 계산
    if -1 not in batting_order and order == 9:
        seq.add(tuple(map(int,batting_order)))
        return

    if order == 3:
        order += 1
    # 순열 만들기
    for ath in range(9):
        if selected[ath] == 0 and batting_order[order] < 0:
            batting_order[order] = ath
            selected[ath] = 1
            get_innings(order+1)
            batting_order[order] = -1
            selected[ath] = 0

get_innings(0)

# 점수 시뮬레이션
for p in list(seq):
    score = 0
    # 현재 타자
    hitter = 0
    for inning in range(N):
        # 아웃 카운터
        out_cnt = 0
        # roo
        roo = [-1] * 3
        while out_cnt < 3:
            player = p[hitter]
            rcd = records[inning][player]
            if rcd == 0: out_cnt += 1
            elif rcd == 1:
                if roo[2] > -1:
                    score += 1
                    roo[2] = -1
                if roo[1] > -1:
                    roo[2] = roo[1]
                    roo[1] = -1
                if roo[0] > -1:
                    roo[1] = roo[0]
                roo[0] = hitter
            elif rcd == 2:
                if roo[2] > -1:
                    score += 1
                    roo[2] = -1
                if roo[1] > -1:
                    score += 1
                    roo[1] = -1
                if roo[0] > -1:
                    roo[2] = roo[0]
                    roo[0] = -1
                roo[1] = hitter
            elif rcd == 3:
                if roo[2] > -1: score += 1
                if roo[1] > -1: score += 1
                if roo[0] > -1: score += 1
                roo = [-1] * 3
                roo[2] = hitter
            elif rcd ==4:
                if roo[2] > -1: score += 1
                if roo[1] > -1: score += 1
                if roo[0] > -1: score += 1
                roo = [-1] * 3
                score += 1
            hitter+=1
            if hitter == 9:
                hitter = 0
    if score > best_record:
        best_record = score
        print('batting_order : ', batting_order, ' score : ', score)
print(best_record)