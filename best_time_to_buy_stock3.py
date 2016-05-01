# reference:
# http://www.cnblogs.com/zuoyuan/p/3766168.html


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_before_i = [0] * len(prices)
        max_after_i = [0] * len(prices)

        cur_min = prices[0]
        for i in range(1, len(prices)):
            max_before_i[i] = max(max_before_i[i - 1], prices[i] - cur_min)
            cur_min = min(cur_min, prices[i])

        cur_max = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            max_after_i[i] = max(max_after_i[i + 1], cur_max - prices[i])
            cur_max = max(cur_max, prices[i])

        global_max = 0
        for i in range(len(prices)):
            global_max = max(global_max, max_before_i[i] + max_after_i[i])

        return global_max


if __name__ == '__main__':
    print(Solution().maxProfit([3, 5, 1, 2, 4, 5, 2, 4]))
