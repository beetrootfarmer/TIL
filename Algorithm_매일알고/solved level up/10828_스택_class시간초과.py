# class base 스택구현
class Stack:

    # stack이 최초 생성될때 필요한 정보들 생성자에 담을 것
    # stack 자료형은 최대 크기가 지정
    def __init__(self, size):
        # stack의 크기
        self.size = size
        # stack에 자료를 저장할 구조
        # stack 처음 만들어질 때 각 요소들은 값이 없어야해서 None으로 초기화
        self.arr = [None] * size
        # stack의 최상단
        self.top = -1

    # stack이 비어있는지 확인하는 메서드
    def is_empty(self):
        if self.top == -1:
            return 1
        else:
            return 0

    # stack에 값을 추가하는 연산
    def push(self, v):
        self.top += 1
        self.arr[self.top] = v

    # stack에 값을 제거하는 연산
    def pop(self):
        if self.is_empty():
            return -1
        else:
            value = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
            return value
    def topp(self):
        if self.is_empty():
            return -1
        return self.arr[self.top]

N = int(input())
stack = Stack(N)
for _ in range(N):
    command = input()
    if command[:4] == 'push':
        stack.push(int(command[5:]))
    elif command == 'top':
        print(stack.topp())
    elif command == 'size':
        print(stack.top + 1)
    elif command == 'empty':
        print(stack.is_empty())
    elif command == 'pop':
        print(stack.pop())
