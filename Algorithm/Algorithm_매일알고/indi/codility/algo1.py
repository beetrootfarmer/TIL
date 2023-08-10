def solution(A):
    # Implement your solution here]
    not_found = True
    unq = -1
    not_unq = set()
    while A and not_found:
        num = A.pop(0)
        nf = 1
        if num in not_unq:
            continue
        for i in range(len(A)):
            # if i == len(A): break
            if A[i] == num:
                not_unq.add(A[i])
                nf = 0
        if nf == 1: not_found = False
        if not_found == False:
            unq = num
            break
    return unq

a = list(map(int,input().split()))
s = solution(a)
print(s)