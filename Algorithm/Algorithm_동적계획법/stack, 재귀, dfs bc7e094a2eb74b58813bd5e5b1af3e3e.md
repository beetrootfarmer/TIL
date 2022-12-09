# DP

### Memoization

메모이제이션은 리스트입니다

- 동적계획법 중 top-down 방식
- 작은 문제로 쪼개면서 해결하는 방식
- bottom-up 과 top-down 차이
    
    ```python
    # bottom-up 형식 
    def fibo(n):
        arr = []
        for i in range(n):
            if i < 2:
                arr.append(1)
            else:
                arr.append((arr[i-1] + arr[i-2]))
        return arr
    print(fibo(10))
    
    # top-down 방식
    def fibo2(n):
        if n >=2 and len(memo) <= n:
            memo.append(fibo2(n-1) + fibo2(n-2))
        return memo[n]
    memo = [0, 1]
    print(fibo(8))
    print(memo)
    ```
    

재귀호출 시 중복을 줄이는 코드

```python
# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# for i in range(56):
#     print(i, fibo(i))

    # 중복호출이 여러번 일어나서 느림
    # 재귀호출 횟수에 중복을 줄이는 형태!
def fibo(n):
    if memo[n] == -1:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

memo = [-1] * 101
memo[0] = 0
memo[1] = 1

for i in range(101):
    print(i, fibo(i))
```

---

# DP (Dynamic Programming)

- 최적화 문제를 해결하는 알고리즘
- **작은 부분 문제를 모두 해결한 후 그 해를 이용해 큰 문제를 해결**
- memoization은 DP의 종류
    - memoization을 기법을 사용해 작은문제의 답을 저장해 놓는다
- 테이블에 값을(해를) 저장

### 분할정복과 비교

- DP는 상향식, 분할정복은 하향식 접근법
- 작은 문제끼리의 중복이 있음(그래서 memoization 사용), 분할정복은 중복이 없음

### dp의 구현방식

- recursive 재귀
- iterative 반복
- 재귀적구조는 시스템 호출스택을 사용하는 오버헤드가 발생하기 때문에 iterative반복이 성능면에서 더 효율적임

- 피보나치 수 DP적용 알고리즘
- 타뷸레이션 tabulation

```python
def fibo2(n):
	f = [0, 1]

	for i in range(2, n+1):
		f.append(f[i-1] + f[i-2])
	
	return f[n]
```

```python
def fibo2(n):
	cache = [0 for i in range(n + 1)]
	cache[0] = 0
	cache[1] = 1

	for i in range(2, n + 1)
		cache[i] = cache[i-1] + cache[i-2]
	return cache[n]
```

- 피보나치 DP

```python
def fibo_dp(n):
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return table                            # return 쓰지 않아도 table 값 바뀌어있지만 명시

table = [0]*101
fibo_dp(100)
print(table[20])

```

- 테이블이 없이 최종값만 필요하다면 이런 방법도 가능

```python
a = 0
b = 1
n = 20
for _ in range(n-1):
    a, b = b, a+b

print(b)
```

### (관련문제1) 2X1 타일링

![스크린샷 2022-12-09 오후 6.30.40.png](stack,%20%E1%84%8C%E1%85%A2%E1%84%80%E1%85%B1,%20dfs%20bc7e094a2eb74b58813bd5e5b1af3e3e/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-12-09_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_6.30.40.png)

✔️ 점화식을 찾는다

`dp[n] = dp[n-1] + dp[n-2]`

```python
# 1. 입력값에 따른 빈 리스트를 만든다
dp = [0] * 1001
# 2. 초기값을 설정한다 ( 0, 1 자리의 값 )
dp[1] = 1
dp[2] = 2
# 3. 점화식 기반으로 계산 값 적용하기
for i in range(3, 1001):
	dp[i] = dp[i - 1] + dp[i - 2]
# 4. 특정 입력값에 따른 계산값을 리스트에서 추출해 반환
print(dp[n])
```

### (관련문제2) 9461 파도반수열

![Untitled](stack,%20%E1%84%8C%E1%85%A2%E1%84%80%E1%85%B1,%20dfs%20bc7e094a2eb74b58813bd5e5b1af3e3e/Untitled.png)

![스크린샷 2022-12-09 오후 6.56.01.png](stack,%20%E1%84%8C%E1%85%A2%E1%84%80%E1%85%B1,%20dfs%20bc7e094a2eb74b58813bd5e5b1af3e3e/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-12-09_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_6.56.01.png)

✔️ 인접한 변을 가진 정삼각형을 연속으로 만드는데 만들어진 순서대로 변의길이를 저장한 수열이 파도반수열

해당 리스트에서 n번째 숫자를 출력하는 문제

✔️ 변의길이가 어떤 규칙성을 가지고 증가하는지 파악하고 리스트를 만든 뒤 출력하는 방식으로 접근(점화식)

```python
T = int(input())
dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1
for i in range(4, 101):
    dp[i] = dp[i - 2] + dp[i - 3]
for _ in range(T):
    n = int(input())
    print(dp[n])
```

### (관련문제3) 1904 01타일

![스크린샷 2022-12-09 오후 7.09.07.png](stack,%20%E1%84%8C%E1%85%A2%E1%84%80%E1%85%B1,%20dfs%20bc7e094a2eb74b58813bd5e5b1af3e3e/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-12-09_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_7.09.07.png)

✔️ 숫자가 증가하는 패턴 파악

✔️ 입력값의 최대 숫자 파악

입력숫자의 최대값이 1,000,000 이고 제한시간이 짧기 때문에 배열에 push하며 만든다

```python
def fibo(n):
	if n <= 2:
		return n
	sm, v1, v2 = 0, 1, 2
	
	for i in range(2, n):
		sm = (v1 + v2) % 15746
		v1 = v2
		v2 = sm
	return sm

print(fibo(int(input())))
```

---