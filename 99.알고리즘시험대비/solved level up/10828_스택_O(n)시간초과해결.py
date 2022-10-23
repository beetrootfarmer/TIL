import sys

input=sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    command = input().strip()
    if command[:4] == 'push':
        stack.append(int(command[5:]))
    elif command == 'top':
        if not stack: print(-1)
        else : print(stack[-1])
    elif command == 'size':
        if not stack: print(0)
        else: print(len(stack))
    elif command == 'empty':
        if not stack: print(1)
        else: print(0)
    elif command == 'pop':
        if not stack: print(-1)
        else: print(stack.pop())
