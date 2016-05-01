from collections import defaultdict


class Solution(object):
    def topo_sort(self, nodes, edges):
        def dfs(v):
            visited.add(v)
            visited_this_call.add(v)
            if v in edges:
                for next in edges[v]:
                    # there is a cycle!!
                    if next in visited_this_call:
                        return False
                    if next not in visited:
                        if not dfs(next):
                            return False
            order.append(v)
            visited_this_call.remove(v)
            return True

        order = []
        visited = set()
        for n in nodes:
            if n not in visited:
                visited_this_call = set()
                if not dfs(n):
                    return ""
        return ''.join(reversed(order))

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return ''
        # if there is only 1 word, any ordering of the letters is good
        if len(words) == 1:
            return words[0]

        # get all the distinct letters
        letters = set()
        for w in words:
            for l in w:
                letters.add(l)

        edges = defaultdict(set)
        for w1, w2 in zip(words, words[1:]):
            # here w1 < w2
            for l1, l2 in zip(w1, w2):
                if l1 != l2:
                    # l1 has to go before l2 in the ordering
                    edges[l1].add(l2)
                    break

        return self.topo_sort(letters, edges)


if __name__ == '__main__':
    words = [
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt",
    ]
    assert Solution().alienOrder(words) == 'wertf'

    # invalid order, should return ""
    words = [
        "a",
        "b",
        "a",
    ]
    assert Solution().alienOrder(words) == ''

    words = [
        "a",
        "b",
        "bad",
        "bc",
        "dc",
        "dd",
    ]
    assert Solution().alienOrder(words) == 'abcd'  # there is another possible order though
