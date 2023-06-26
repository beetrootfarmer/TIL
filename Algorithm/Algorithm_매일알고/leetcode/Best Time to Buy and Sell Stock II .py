# stock을 사고팔아서 낼 수 있는 가장 높은 수익을 리턴하는 문제
# 기간동안의 가격 리스트를 순회하는 방식으로 해결했기때문에
# 시간복잡도는 O(N)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # stock에는 1개만 있을 수 있음
        # 사고 파는 과정은 1개씩만 진행할 수 있음

        # price를 순회하면서 min가격보다 클 경우 팔아서 수익을 더해줌
        minP = max(prices) + 1
        profit = 0
        for p in prices:
            # 낮은 가격을 갱신하고
            minP = min(p, minP)
            # 현재 가격이 낮은가격보다 높을경우 판매
            if p - minP > 0:
                profit += p - minP
                # 현재가격을 minP로 설정
                minP = p
        return profit
