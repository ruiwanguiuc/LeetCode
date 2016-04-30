# reference
# https://segmentfault.com/a/1190000003797204


class Solution(object):

    all_res = []

    def dfs(self, num, cur_exp, cur_res, prev_num, target):
        if not num and cur_res == target:
            Solution.all_res.append(cur_exp)
            return
        for i in range(1, len(num) + 1):
            next = num[:i]
            rest = num[i:]
            next_num = int(next)
            if len(next) > 1 and next[0] == '0':
                # here we just return since if this next starts with 0 all the following
                # exploration will also give the next number that starts with 0
                return
            if cur_exp:
                self.dfs(rest, cur_exp + '+' + next, cur_res + next_num, next_num, target)
                self.dfs(rest, cur_exp + '-' + next, cur_res - next_num, -next_num, target)
                res = (cur_res - prev_num) + (prev_num * next_num)
                self.dfs(rest, cur_exp + '*' + next, res, prev_num * next_num, target)
            else:
                self.dfs(rest, next, next_num, next_num, target)

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        Solution.all_res = []
        self.dfs(num, '', 0, 0, target)
        return Solution.all_res


# below is my naive solution
# class Solution(object):
#     """
#     Given a string that contains only digits 0-9 and a target value, return all
#     possibilities to add binary operators (not unary) +, -, or * between the digits
#     so they evaluate to the target value.

#     e.g.
#     "123", 6 -> ["1+2+3", "1*2*3"]
#     "232", 8 -> ["2*3+2", "2+3*2"]
#     "105", 5 -> ["1*0+5","10-5"]
#     "00", 0 -> ["0+0", "0-0", "0*0"]
#     "3456237490", 9191 -> []
#     """
#     def eval(self, exp):
#         # split exp into tokens
#         digit_start = 0
#         tokens = []
#         for i, char in enumerate(exp[1:], start=1):
#             if char in ('+', '-', '*'):
#                 tokens.append(int(exp[digit_start:i]))
#                 tokens.append(exp[i])
#                 digit_start = i + 1
#         tokens.append(int(exp[digit_start:]))

#         # resolve all multiplications
#         new_tokens = [tokens[0]]
#         i = 1
#         while i < len(tokens):
#             if tokens[i] == '*':
#                 cur = new_tokens.pop()
#                 cur *= tokens[i + 1]
#                 i += 2
#                 new_tokens.append(cur)
#             else:
#                 new_tokens.append(tokens[i])
#                 i += 1

#         # eval + and -
#         i = 1
#         res = new_tokens[0]
#         while i < len(new_tokens):
#             if new_tokens[i] == '+':
#                 res += new_tokens[i + 1]
#                 i += 2
#             else:
#                 res -= new_tokens[i + 1]
#                 i += 2
#         return res

#     def addOperators(self, num, target):
#         """
#         :type num: str
#         :type target: int
#         :rtype: List[str]
#         """
#         all_sol = []

#         def dfs(exp_so_far, exp_left):
#             # print exp_so_far + '|' + exp_left
#             if not exp_left:
#                 if eval(exp_so_far) == target:
#                     all_sol.append(exp_so_far)
#             elif len(exp_left) == 1:
#                 dfs(exp_so_far + exp_left, '')
#             else:
#                 if exp_so_far and exp_so_far[-1] in ('+', '-', '*') and exp_left[0] == '0':
#                     dfs(exp_so_far + '0+', exp_left[1:])
#                     dfs(exp_so_far + '0-', exp_left[1:])
#                     dfs(exp_so_far + '0*', exp_left[1:])
#                 else:
#                     dfs(exp_so_far + exp_left[0] + '+', exp_left[1:])
#                     dfs(exp_so_far + exp_left[0] + '-', exp_left[1:])
#                     dfs(exp_so_far + exp_left[0] + '*', exp_left[1:])
#                     dfs(exp_so_far + exp_left[0], exp_left[1:])

#         dfs('', num)
#         return all_sol


if __name__ == "__main__":
    print(Solution().addOperators('105', 5))
