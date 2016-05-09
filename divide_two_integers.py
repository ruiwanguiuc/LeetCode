class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            raise ZeroDivisionError
        if dividend == 0:
            return 0
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend < divisor:
            return 0
        total_count = 0
        while dividend >= divisor:
            count = 1
            cur_sum = divisor
            while cur_sum + cur_sum <= dividend:
                cur_sum += cur_sum
                count += count
            dividend -= cur_sum
            total_count += count
        return total_count if sign == 1 else 0 - total_count


if __name__ == "__main__":
    print(Solution().divide(40, -3))
    print(Solution().divide(4, 1))
    print(Solution().divide(0, -3))
    print(Solution().divide(2, 3))
    print(Solution().divide(-1, 1))
    print(Solution().divide(20, 3))
