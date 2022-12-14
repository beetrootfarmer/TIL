# 최소 신장 트리(MST)

- 그래프에서 최소 비용 문제
    - 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
    - 두 정점 사이의 최소 비용의 경로 찾기
- 신장 트리
    - n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이뤄진 트리
- 최소 신장 트리(Minimum Spanning Tree)
    - 무방향 가중치 그래프에서 신장트리를 구성하는 간선들의 가중치의 합이 최소인 신장트리

```python
V, E = map(int, input().split())
adjM = [[0]*(V+1) for _ in  range(V+1)]
adjL = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w

    #인점 리스트 방식
    adjL[u].append((v, w))
    adjL[v].append((u,w))
```

## Prim 알고리즘

- 하나의 정점에서 연결된 간선들 중에 하나씩 선택하며 MST를 만들어가는 방식
    1. 임의의 정점을 하나 선택해서 시작
    2. 선택한 정점과 인접하는 정접들 중 최소비용의 간선이 존재하는 정점을 선택
    3. 모든 정점이 선택될때까지 1, 2를 반복
- 프림 알고리즘이 동작하기 위해서는 두 종류의 상호배타집합들의 정보가 필요
    - 트리 정점들(tree vertices) - MST를 만들기 위해 선택된 정점들
    - 비트리 정점들(nontree vertices) - 선택되지 않은 정점들

prim 코드로 표현하는 방법

1. 

```python
def prim1(r, V):
    MST = [0] * (V+1)           # MST 포함여부를 확인하기 위한 리스트
    key = [10000] * (V+1)       # 가중치의 최대값으로 초기화. key[v]는 v가 MST에 속한 정점과연결된다
    key[r] = 0                  # 시작정점의 key 
    for i in range(V):          # V+1개의 정점 중 V개를 선택 
        u = 0                   # MST에 포함되지 않는 정점 중 (MST[u]==0) key가 최소인 u 찾기 
        minV = 10000
        if MST[i] == 0 and key[i] < minV:
            u = i
            minV = key[i]
        MST[u] = 1
        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v] > 0:
                key[v] = min(key[v] , adjM[u][v])
    return sum(key)             # MST의 가중치의 합

V, E =map(int, input().split())
adjM = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w
print(prim1(0, V))
```

1. 

```python
def prim2(r, V):
    MST = [0] *(V+1)        # MST 포함 여부
    MST[r] = 1              # 시작정점 포함 표시
    s = 0                   # MST 간선의 가중치 합 
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 1:
                for j in range(V+1):
                    if adjM[i][j] > 0 and MST[j] == 0 and minV> adjM[i][j]:
                        u = j
                        minV = adjM[i][j]

        s += minV
        MST[u] = 1
    return s

V, E =map(int, input().split())
adjM = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w
print(prim2(0, V))
```

---

## KRUSKAL 알고리즘

- 간선을 하나씩 선택해서 MST를 찾는 알고리즘
1. 최초 모든 간선을 가중치에 따라 오름차순 정렬
2. 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴
    
    사이클이 존재하면 다음으로 가중치가 낮은 간선 선택
    
    ⇒ find set 을 활용해서 서로 다른 대표원소를 가진 간선을 이어줌
    
3. n-1개의 간선이 선택될 때까지 2를 반복 

```python
# 자기 자신을 가르키는 대표원소를 찾는 find set
def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

# x의 대표원소를 y의 대표원소로
def union(x, y):
    rep[find_set(y)] = find_set(x)

V, E = map(int, input().split())
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([w, u, v])
edge.sort()
rep = [i for i in range(V + 1)]         # 대표원소 배열 

N = V + 1       # 실제 정점 수 
cnt = 0         # 선택한 edge의 수 
total = 0
for w, u, v in edge:
    if find_set[u] != find_set(v):
        cnt += 1
        union(u, v)
        total += w
        if cnt == N-1:
            break
print(total)
```