class Solution(object):
    def get_unpaired_p(self, s):
        count = 0
        r_unpaired = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                if count == 0:
                    r_unpaired += 1
                else:
                    count -= 1
        return count + r_unpaired

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(string):
            visited.add(string)
            unpaired = self.get_unpaired_p(string)
            if unpaired == 0:
                return [string]
            ret = []
            for i in range(len(string)):
                if string[i] in ('(', ')'):
                    removed = string[:i] + string[i + 1:]
                    if removed not in visited and self.get_unpaired_p(removed) < unpaired:
                        ret.extend(dfs(removed))
            return ret

        visited = set([])
        return dfs(s)


if __name__ == "__main__":
    # print(Solution().get_unpaired_p('(a)())()'))
    # print(Solution().get_unpaired_p(')a('))
    print Solution().removeInvalidParentheses('(a)())()')
