# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    # Implement your solution here

    cost = 0
    idx = 0
    while idx < len(S) - 1:
        comp = idx + 1
        if C[idx] == -1:
            continue
        if C[comp] == -1:
            while C[comp] == -1:
                comp += 1
        if S[idx] == S[comp]:
            if C[idx] > C[comp]:
                cost += C[comp]
                C[comp] = -1
            else:
                cost += C[idx]
                C[idx] = -1
                idx += 1
        else:
            idx += 1
    print(cost)
    return cost
solution('aabbcc',[1,2,1,2,1,2])
# print(solution('aabbcc',[1,2,1,2,1,2]))