from collections import defaultdict


class Solution(object):

    def topo_sort(self, nodes, edges):
        def dfs(n):
            visited.add(n)
            visited_this_call.add(n)
            if n in edges:
                for next in edges[n]:
                    if next in visited_this_call:
                        return False
                    if next not in visited:
                        if not dfs(next):
                            return False
            order.append(n)
            visited_this_call.remove(n)
            return True

        order = []
        visited = set()
        for n in nodes:
            if n not in visited:
                visited_this_call = set()
                if not dfs(n):
                    return []
        return list(reversed(order))

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        edges = defaultdict(list)
        for course, prereq in prerequisites:
            edges[prereq].append(course)
        return self.topo_sort(range(numCourses), edges)


if __name__ == "__main__":
    print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
