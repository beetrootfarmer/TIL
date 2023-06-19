import sys
input = sys.stdin.readline

# 좋은 염기서열의 개수 N과 서열의 길이 M
N, M = map(int,input().split())
# M길이의 배열을 만들고 배열의 자리마다 필요한 중복 제외 글자를 카운트하기위한 배
counter = [0]*M

# 좋은 염기서열 리스트
pos = list(input().strip() for _ in range(N))

# 좋은 염기서열 리스트의 글자마다 순회하며 counter 배열을 채움
for p in range(N):
    for m in range(M):
        if pos[p][m] != '.':
            if counter[m] == 0:
                counter[m] = set(list(pos[p][m]))
            elif pos[p][m] not in counter[m]:
                counter[m].add(pos[p][m])

# 최소한 필요한 글자수
min_word = 1         # 모두 와일드카드일 경우 min_word는 1이 되어야함

# counter 순회하면서 가장 긴 배열 길이를 min_word에 갱신
for c in counter:
    if c == 0:
        continue
    if len(c) > min_word:
        min_word = len(c)


print(min_word)
