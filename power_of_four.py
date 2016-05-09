class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # naive solution
        # if num <= 0:
        #     return False
        # while num > 1:
        #     if num % 4 != 0:
        #         return False
        #     num = num / 4
        # return num == 1

        # optimal solution
        return num > 0 and num & (num - 1) == 0 and num & 0x55555555 != 0


if __name__ == '__main__':
    print(Solution().isPowerOfFour(4))
    print(Solution().isPowerOfFour(0))
    print(Solution().isPowerOfFour(64))
    print(Solution().isPowerOfFour(32))
    print(Solution().isPowerOfFour(2))
    print(Solution().isPowerOfFour(12))
