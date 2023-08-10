import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    data_len, start = map(int, input().split())
    data = [[] for _ in range(101)]                  # 연락 최대인원 100이하
    inp = list(map(int, input().split()))
    for i in range(0,data_len,2):                    # from 짝수 번호를 인덱스번호로 하는 data 리스트를 생성
        data[inp[i]].append(inp[i+1])                # 해당 인덱스번호에 to 정보가 담겨있음
    # print(data)
    last = []                                        # 마지막에 연락이 닿은 숫자를 담아줌
    last.append([start])
    idx = 1
    # next에 연결된 연락망만큼 for문을 돌림
    # 현재시점에 연락이 닿은 사람을 담아줌
    end = 0
    visited = [[] for _ in range(101)]
    while True:
        next = []
        cnt = 0
        for j in last[-1]:
            if len(data[j]) != 0:
                break
            else:
                cnt += 1
        if cnt == len(last[-1]):
            break

        for i in last[-1]:
            for j in data[i]:
                if visited[j]:
                    continue
                next.append(j)
                visited[j] = 1
            data[i] = []

        last.append(next)
        idx += 1
    # print(last)
    while not last[-1]:
        last.pop(-1)
    print(f'#{tc} {max(last[-1])}')
    # print()
