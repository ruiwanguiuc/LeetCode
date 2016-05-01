class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # This is clearer but uses kn memory.
        # if not prices:
        #     return 0
        # l = len(prices)
        # dp = [[0] * l for i in range(k + 1)]
        # for kk in range(1, k + 1):
        #     local_max = dp[kk - 1][0] - prices[0]
        #     for j in range(1, l):
        #         dp[kk][j] = max(
        #             dp[kk][j - 1],
        #             local_max + prices[j]
        #         )
        #         local_max = max(local_max, dp[kk - 1][j] - prices[j])
        # return dp[k][-1]

        # This only uses n memory since we only need dp[k - 1][:] when computing dp[k][:]
        if not prices:
            return 0
        l = len(prices)
        if k > l / 2:
            return self.quickSolve(l, prices)
        dp = [0] * l
        for kk in range(1, k + 1):
            # here dp holds all the values from k - 1
            local_max = dp[0] - prices[0]
            for j in range(1, l):
                # here dp[:j] holds the values for current k but dp[j:] still holds
                # k - 1 dp values
                # we need to put it in a temp variable since we still need dp[k - 1][j]
                # in the next line
                tmp_dp = max(
                    dp[j - 1],
                    local_max + prices[j]
                )
                local_max = max(local_max, dp[j] - prices[j])
                dp[j] = tmp_dp
        return dp[-1]

    def quickSolve(self, size, prices):
        sum = 0
        for x in range(size - 1):
            if prices[x + 1] > prices[x]:
                sum += prices[x + 1] - prices[x]
        return sum


if __name__ == '__main__':
    print(Solution().maxProfit(2, [3, 5, 1, 2, 4, 5, 2, 4]))