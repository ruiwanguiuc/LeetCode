from collections import defaultdict


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        edges_dict = defaultdict(list)
        for e in edges:
            edges_dict[e[0]].append(e[1])
            edges_dict[e[1]].append(e[0])

        def dfs(node, prev):
            # use prev here since this is undirected graph and we want
            # to avoid travel back using the same edge.
            visited.add(node)
            if node in edges_dict:
                for next in edges_dict[node]:
                    if next == prev:
                        continue
                    if next in visited:
                        return False
                    if not dfs(next, node):
                        return False
            return True

        # here since any connected graph without simple cycles is a tree
        # we can just do dfs starting at any node.
        visited = set()
        if not dfs(0, None):
            return False
        return len(visited) == n


if __name__ == '__main__':
    print(Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
    print(Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
