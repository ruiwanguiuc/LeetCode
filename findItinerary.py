from collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if not tickets:
            return []
        by_from = defaultdict(list)
        for t in tickets:
            by_from[t[0]].append(t[1])
        by_from = {f: sorted(t) for f, t in by_from.iteritems()}
        Solution.it = None
        self.dfs(by_from, ['JFK'])
        return Solution.it

    def dfs(self, by_from, cur_it):
        if not by_from:
            Solution.it = cur_it
        cur = cur_it[-1]
        if cur not in by_from:
            return
        nextstops = by_from[cur][:]
        if len(nextstops) == 1:
            del by_from[cur]
            self.dfs(by_from, cur_it + [nextstops[0]])
            by_from[cur] = nextstops
        else:
            for n in nextstops:
                by_from[cur].remove(n)
                self.dfs(by_from, cur_it + [n])
                by_from[cur] = nextstops


if __name__ == "__main__":
    import ipdb;ipdb.set_trace()
    print Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
