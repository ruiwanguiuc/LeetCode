from collections import defaultdict


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        out = defaultdict(list)
        for p, q in prerequisites:
            out[q].append(p)

        visited = [False] * numCourses
        global current_label
        current_label = numCourses
        labels = {}
        res = []

        def dfs(v):
            visited[v] = True
            for n in out[v]:
                if not visited[n]:
                    dfs(n)
            global current_label
            labels[v] = current_label
            current_label -= 1
            res.append(v)

        for c in range(numCourses):
            if not visited[c]:
                dfs(c)

        valid = True
        for p, q in prerequisites:
            if labels[p] < labels[q]:
                valid = False
        if valid:
            return list(reversed(res))
        else:
            return []


if __name__ == "__main__":
    print(list(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])))
