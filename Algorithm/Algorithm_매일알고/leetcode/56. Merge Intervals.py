def merge(intervals):


# 리스트가 정렬이 되어있는지 확인
# 연속된 리스트와 숫자범위가 겹치는지 확인
# 겹친다면 병합

# 시간복잡도 O(N)

    intervals = sorted(intervals)
    i = 0
    for _ in range(len(intervals) - 1):
        # intervals[i]와 인접한 뒤의 리스트를 비교
        now, next = intervals[i], intervals[i + 1]
        if now[1] >= next[0]:
            mg = [min(now[0], next[1]), max(now[1], next[1])]
            intervals[i + 1] = mg
            intervals.pop(i)
        else:
            i += 1
    return intervals

a = merge([[1,4],[4,5]])
print(a)