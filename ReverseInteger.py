class Solution:
    # @return an integer
    def reverse(self, x):
        neg = False
        if x<0:
            neg = True
            x = -x
        ret = 0
        while x>0:
            ret = ret*10+x%10
            x = x/10
        if neg:
            return -ret
        else:
            return ret

if __name__ == "__main__":
    print Solution().reverse(74323)
    print Solution().reverse(103)
    print Solution().reverse(10)
    print Solution().reverse(-1)
    print Solution().reverse(-753)
    print Solution().reverse(0)