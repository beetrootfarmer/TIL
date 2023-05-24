# Example test:   (1, (2, None, (4, None, None)), (3, (5, (7, None, None), (8, None, None)), (6, (9, None, None), (10, (11, None, None), None))))
# Output (stderr):
# Invalid result type, int expected, <class 'NoneType'> found.
# Output:
# Tree(x=1, l=Tree(x=2, l=None, r=Tree(x=4, l=None, r=None)), r=Tree(x=3, l=Tree(x=5, l=Tree(x=7, l=None, r=None), r=Tree(x=8, l=None, r=None)), r=Tree(x=6, l=Tree(x=9, l=None, r=None), r=Tree(x=10, l=Tree(x=11, l=None, r=None), r=None))))
# RUNTIME ERROR (tested program terminated with exit code 1)
#
# Your test case: (1, (2, None, (4, None, None)), (3, (5, (7, None, None), (8, None, None)), (6, (9, None, None), (10, (11, None, None), None))))
# Output (stderr):
# Invalid result type, int expected, <class 'NoneType'> found.
# Output:
# Tree(x=1, l=Tree(x=2, l=None, r=Tree(x=4, l=None, r=None)), r=Tree(x=3, l=Tree(x=5, l=Tree(x=7, l=None, r=None), r=Tree(x=8, l=None, r=None)), r=Tree(x=6, l=Tree(x=9, l=None, r=None), r=Tree(x=10, l=Tree(x=11, l=None, r=None), r=None))))
# RUNTIME ERROR (tested program terminated with exit code 1)

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Tree  # library with types used in the task
from collections import deque


class Node:
    def _init_(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def solution(T):
    def isBT(root):
        if root is None:
            return True
        q = deque()
        q.append(root)

        flag = False
        while (q):
            front = q.popleft()

            if flag and (front.left or front.right):
                return False

            if front.left is None and front.right:
                return False

            if front.left:
                q.append(front.left)
            else:
                flag = True
        return True

    # 노드 root를 순회하며 이진트리인지 확인하고 최대값을 리턴

    print(T)
