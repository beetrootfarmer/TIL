import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for _ in range(T):
    a = deque(input())
    stack = []
    result = 'YES'
    while a:
        open = a.popleft()
        if open != '(':
            if not stack:
                result = 'NO'
            else:
                stack.pop()
        else:
            stack.append(open)
    if stack:
        result = 'NO'
    print(result)