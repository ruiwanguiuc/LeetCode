from collections import deque


class Operator(object):

    @property
    def notation(self):
        raise NotImplementedError

    @staticmethod
    def execute(operand_stack):
        raise NotImplementedError


class Plus(Operator):

    @staticmethod
    def execute(operand_stack):
        second = operand_stack.pop()
        first = operand_stack.pop()
        operand_stack.append(first + second)


class Minus(Operator):

    @staticmethod
    def execute(operand_stack):
        second = operand_stack.pop()
        first = operand_stack.pop()
        operand_stack.append(first - second)


class Multiply(Operator):

    @staticmethod
    def execute(operand_stack):
        second = operand_stack.pop()
        first = operand_stack.pop()
        operand_stack.append(first * second)


class Divide(Operator):

    @staticmethod
    def execute(operand_stack):
        second = operand_stack.pop()
        first = operand_stack.pop()
        res = abs(first) / abs(second)
        if (first < 0 and second > 0) or (first > 0 and second < 0):
            operand_stack.append(-res)
        else:
            operand_stack.append(res)


class OperatorFactory(object):

    notation_to_operator = {
        '+': Plus,
        '-': Minus,
        '*': Multiply,
        '/': Divide
    }

    @staticmethod
    def create(notation):
        if notation not in OperatorFactory.notation_to_operator:
            raise RuntimeError
        return OperatorFactory.notation_to_operator[notation]

    @staticmethod
    def register(notation, operator_cls):
        OperatorFactory.notation_to_operator[notation] = operator_cls


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operands = deque()
        factory = OperatorFactory()

        for t in tokens:
            if t not in ('+', '-', '*', '/'):
                operands.append(int(t))
            else:
                factory.create(t).execute(operands)
        return operands.pop()


# naive solution

# class Solution(object):
#     def evalRPN(self, tokens):
#         """
#         :type tokens: List[str]
#         :rtype: int
#         """
#         operands = deque()
#         for t in tokens:
#             if t == '+':
#                 second = operands.pop()
#                 first = operands.pop()
#                 operands.append(first + second)
#             elif t == '-':
#                 second = operands.pop()
#                 first = operands.pop()
#                 operands.append(first - second)
#             elif t == '*':
#                 second = operands.pop()
#                 first = operands.pop()
#                 operands.append(first * second)
#             elif t == '/':
#                 second = operands.pop()
#                 first = operands.pop()
#                 res = abs(first) / abs(second)
#                 if (first < 0 and second > 0) or (first > 0 and second < 0):
#                     operands.append(-res)
#                 else:
#                     operands.append(res)
#             else:
#                 operands.append(int(t))
#         return operands.pop()


if __name__ == "__main__":
    print(Solution().evalRPN(["10", "6", "-132", "/", "*"]))
