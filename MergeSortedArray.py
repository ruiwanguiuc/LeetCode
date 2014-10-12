# https://oj.leetcode.com/problems/merge-sorted-array/

# Given two sorted integer arrays A and B, merge B into A as one sorted array.
# Note:
# You may assume that A has enough space (size that is greater or equal to m + n)
# to hold additional elements from B. The number of elements initialized in A and
# B are m and n respectively.
class Solution:
    
    def merge(self, A, m, B, n):
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
        m, n = m - 1, n - 1
        i = len(A) - 1
        while m >= 0 and n >= 0:
            if A[m] < B[n]:
                A[i] = B[n]
                n -= 1
            else:
                A[i] = A[m]
                m -= 1
            i -= 1
        if m == -1:
            A[:n+1] = B[:n+1]


if __name__ == "__main__":
    A = [1,3,4,None,None]
    B = [2,5]
    Solution().merge(A,3,B,2)
    print A