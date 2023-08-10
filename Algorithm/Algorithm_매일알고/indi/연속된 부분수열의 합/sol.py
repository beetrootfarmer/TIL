seq = []
res = []


def dfs(arr, sumarr, k, visited):
    global res,seq

    if sumarr == k:
        if res:
            if len(res) > len(arr):
                res = arr
        elif not res:
            res = arr
        return

    for i in range(len(seq)):
        if not arr:
            if not visited[i]:
                visited[i] = 1
                arr.append(i)
                dfs(arr,seq[i], k, visited)
                # visited[i] = 0
                arr.pop()
        else:
            last = arr[-1]
            if arr and last + 1 == i:
                temp = sumarr + seq[i]
                if temp > k:
                    break
                if not visited[i] and temp <= k:
                    visited[i] = 1
                    arr.append(i)
                    dfs(arr, temp, k, visited)
                    # visited[i] = 0
                    arr.pop()


def solution(sequence, k):
    global seq, res
    seq = sequence
    visited = [0] * len(sequence)
    dfs([], 0, k, visited)
    answer = res
    print(res)
    return answer

solution([7,3,4],7)