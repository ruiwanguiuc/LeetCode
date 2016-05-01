class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d_to_l = {
            '1': ['*'],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        if not digits:
            return []
        cur_list = ['']
        for d in digits:
            new_list = []
            for l in d_to_l[d]:
                for ele in cur_list:
                    new_list.append(ele + l)
            cur_list = new_list
        return cur_list
