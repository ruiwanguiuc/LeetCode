import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        prev = sys.maxint
        profit = 0
        for p in prices:
            if p > prev:
                profit += p - prev
            prev = p
        return profit
