from collections import deque

def solution(arrA, arrB):
    answer = False
    arr = deque(arrA[0:-1])
    arr.appendleft(arrA[-1])
    if list(arr) == arrB:
        return True
    else:
        while list(arr) != arrA:
            if arr == arrB:
                answer = True
                break
            else:
                last = arr.pop()
                arr.appendleft(last)

    return answer

res = solution([7,8,10],[10,7,8])
print(res)
