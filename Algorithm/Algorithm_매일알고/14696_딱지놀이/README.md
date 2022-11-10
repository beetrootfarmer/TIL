## BOJ 14696 딱지놀이
---
## 접근방법
- 게임 수 N만큼 반복하면서 두 참가자의 입력을 받는다
- win_or_lose() 함수에 두 입력을 보낸다
- 4-3-2-1 순으로 더 많이 가진 참가자가 있으면 승부가 결정된다
---
## 코드
```python
N = int(input()) # 총 라운드 수
child1 = [[] for _ in range(N)]
child2 = [[] for _ in range(N)]

def win_or_lose(c1, c2):
    sa = c1.pop(0)
    sa2 = c2.pop(0)
    # 4-3-2-1 비교
    for num in range(4, 0, -1):
        cnt1, cnt2 = 0, 0
        while num in c1:
            c1.remove(num)
            cnt1 += 1
        while num in c2:
            c2.remove(num)
            cnt2 += 1
        if cnt1 == cnt2:
            continue
        elif cnt1 > cnt2:
            return 'A'
        else:
            return 'B'
    return 'D'


for i in range(N):
    child1[i] = list(map(int, input().split()))
    child2[i] = list(map(int,input().split()))
    print(win_or_lose(child1[i], child2[i]))

```