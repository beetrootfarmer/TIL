# 리스트로 기둥의 높이가 주어지고
# 가장 넓은 사각형을 만들 수 있는 기둥의 시작점,끝점을 확인하고
# 가장 넓은 사각형의 넓이를 리턴하는 함수

# 1) 리스트를 2중 for문으로 순회하면서 경우의수를 확인하는 방법을 사용하면 O(N^2)
#       61개의 테스트케이스 중 51개가 통과하고 시간초과가 난다
# 2) 시간을 줄이기위해서 slidingwindow 방법을 사용
#       2개의 포인트를 끝에서 시작해 더 값이 작은쪽(더 큰 값을 만들 가능성이 없는 경우)을 줄여나가면서 사용하는 방법
#       위 방법을 사용할 경우 시간복잡도는 O(N)

class Solution:
    def maxArea(self, height):
        maxA = 0
        hlen = len(height)
        for h in range(hlen-1):
            for h2 in range(h+1, hlen):
                area = min(height[h], height[h2]) * h2-h
                maxA = max(area, maxA)
        return maxA
# 2)
class Solution:
    def maxArea(self, height):
        maxA = 0
        s,e = 0, len(height)-1
        while s != e:
            if height[s] < height[e]:
                area = min(height[s],height[e]) * (e-s)
                maxA = max(area, maxA)
                s+=1
            else:
                area = min(height[s],height[e]) * (e-s)
                maxA = max(area,maxA)
                e -= 1
        return maxA