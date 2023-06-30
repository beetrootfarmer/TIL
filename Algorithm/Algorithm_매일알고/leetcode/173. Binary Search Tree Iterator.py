# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# in-order 방식의 트리 순회 : root의 좌측에 있는 노드, root, 우측노드를 순서대로 순회하는 방식
# 입력받는 데이터의 형태를 파악하기가 어려움

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = list()
        # 좌측의 노드를 탐색해서 노드에 담는다
        # root부터 왼쪽에 존재하는 모든 노드가 담기고 마지막 노드가 첫번째 순회노드가 된다
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        :rtype: int
        """
        # stack에 담은 노드를 마지막에서부터 꺼내고
        # 현재 노드에서 우측에 위치한 노드를 stack에 담는다
        nowNode = self.stack.pop()
        r = nowNode.right
        while r:
            self.stack.append(r)
            r = r.left

        return nowNode.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()