# 리스트 클래스를 구현하는 문제
# 리스트 insert, delete, getrandom 처리를 O(1)로 구현해야함
# append, pop, randrange를 이용
# O(1) : 데이터 갯수에 상관없이 항상 일정한 단계의 알고리즘이 필요, 상수시간을 갖는 알고리즘
# 반면 O(N) : 데이터 증가가 성능에 영향을 미친다. 배열 원소가 N개일때 N단계가 걸리는 알고리즘
# O(logN) 은 N의 원소가 있을 때 log2N이다. N이 8이면 3. 데이터가 두 배로 증가할 때마다 한 단계씩 늘어나는 알고리즘

from random import randrange

class RandomizedSet:

    def __init__(self):
        self.data = []

    def insert(self, val: int) -> bool:
        # 리스트에 존재하면 false 리턴
        if val in self.data:
            return False
        # 리스트에 존재하지 않으면 insert 하고 True 리턴
        else:
            # append는 O(1)
            self.data.append(val)
            return True

    def remove(self, val: int) -> bool:
        # 리스트에 존재하면 remove하고 true 리턴
        # 리스트 전체순회를 하기때문에 O(N)
        for i in range(len(self.data)):
            if self.data[i] == val:
                # 특정 인덱스를 추출하는 pop은 O(N)
                self.data.pop(i)
                return True
        # 리스트에 존재하지 않으면 false 리턴
        else:
            return False

    def getRandom(self) -> int:
        # len()은 O(1)
        i = randrange(len(self.data))  # 0부터 self길이-1 사이의 임의의 정수
        return self.data[i]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()