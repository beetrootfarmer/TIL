from copy import deepcopy
class Node:
    def _init_(self, next=None, random=None):
        self.val = int()
        self.next = next
        self.random = random

def copyRandomList(head):
	# result = []
	# for h in head:
	# 	val, random = h.val, h.random
	# 	result.append([val, random])
    result = deepcopy(head)
    return result


nd = [[7,None],[13,0],[11,4],[10,2],[1,0]]
arr = []
for n in nd:
    nn = Node()
    nn.val = n[0]
    nn.random  = n[1]
    arr.append(nn)
a = copyRandomList(arr)
print(a)