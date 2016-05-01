import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_value = sys.maxint
        current_max = -1
        for p in prices:
            min_value = min(p, min_value)
            if p - min_value > current_max:
                current_max = p - min_value
        return current_max
