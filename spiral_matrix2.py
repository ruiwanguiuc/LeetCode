class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 1:
            return [[]]
        if n == 1:
            return [[1]]
        if n == 2:
            return [[1, 2], [4, 3]]
        mat = [[0] * n for i in range(n)]
        i = j = 0
        cur = 1
        dir = 'r'
        while True:
            mat[i][j] = cur
            if 1 <= i and i < n - 1 and 1 <= j and j < n - 1 and mat[i - 1][j] != 0 and mat[i + 1][j] != 0 and \
                    mat[i][j - 1] != 0 and mat[i][j + 1] != 0:
                return mat
            if dir == 'r':
                if j < n - 1 and mat[i][j + 1] == 0:
                    j += 1
                    cur += 1
                else:
                    dir = 'd'
            elif dir == 'd':
                if i < n - 1 and mat[i + 1][j] == 0:
                    i += 1
                    cur += 1
                else:
                    dir = 'l'
            elif dir == 'l':
                if j > 0 and mat[i][j - 1] == 0:
                    j -= 1
                    cur += 1
                else:
                    dir = 'u'
            elif dir == 'u':
                if i > 0 and mat[i - 1][j] == 0:
                    i -= 1
                    cur += 1
                else:
                    dir = 'r'


if __name__ == "__main__":
    # import ipdb;ipdb.set_trace()
    print Solution().generateMatrix(3)
