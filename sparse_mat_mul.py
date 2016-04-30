from collections import defaultdict


class Solution(object):
    def sparsify(self, mat):
        sp_dict = defaultdict(dict)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    sp_dict[i][j] = mat[i][j]
        return sp_dict

    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        # regular matrix multiplication
        # if not A or not A[0] or not B or not B[0]:
        #     return [[]]
        # rowa = len(A)
        # cola = len(A[0])
        # rowb = len(B)
        # colb = len(B[0])
        # ret = [[0] * colb for i in range(rowa)]
        # for i in range(rowa):
        #     for j in range(colb):
        #         for x in range(cola):
        #             ret[i][j] += A[i][x] * B[x][j]
        # return ret

        # accepted solution
        if not A or not A[0] or not B or not B[0]:
            return [[]]
        rowa = len(A)
        cola = len(A[0])
        rowb = len(B)
        colb = len(B[0])
        table_a = self.sparsify(A)
        table_b = self.sparsify(B)
        ret = [[0] * colb for i in range(rowa)]
        for i in table_a:
            for j in table_a[i]:
                if j not in table_b:
                    continue
                for k in table_b[j]:
                    ret[i][k] += table_b[j][k]
        return ret


if __name__ == "__main__":
    A = [
        [1, 0, 0],
        [-1, 0, 3]
    ]
    B = [
        [7, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    print(Solution().multiply(A, B))
