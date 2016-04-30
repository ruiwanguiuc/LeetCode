class Solution(object):
    def digitToWord(self, digit):
        result = ''
        if digit == 1:
            result += 'One'
        elif digit == 2:
            result += 'Two'
        elif digit == 3:
            result += 'Three'
        elif digit == 4:
            result += 'Four'
        elif digit == 5:
            result += 'Five'
        elif digit == 6:
            result += 'Six'
        elif digit == 7:
            result += 'Seven'
        elif digit == 8:
            result += 'Eight'
        elif digit == 9:
            result += 'Nine'
        return result

    def numberToWordsInThousand(self, num):
        hundred = num / 100
        ten = (num % 100) / 10
        one = num % 10
        result = ''
        if hundred > 0:
            result += self.digitToWord(hundred) + ' Hundred'
        if ten == 1:
            if one == 0:
                result += ' Ten'
            elif one == 1:
                result += ' Eleven'
            elif one == 2:
                result += ' Twelve'
            elif one == 3:
                result += ' Thirteen'
            elif one == 4:
                result += ' Fourteen'
            elif one == 5:
                result += ' Fifteen'
            elif one == 6:
                result += ' Sixteen'
            elif one == 7:
                result += ' Seventeen'
            elif one == 8:
                result += ' Eighteen'
            elif one == 9:
                result += ' Nineteen'
            return result.strip()
        elif ten == 2:
            result += ' Twenty'
        elif ten == 3:
            result += ' Thirty'
        elif ten == 4:
            result += ' Forty'
        elif ten == 5:
            result += ' Fifty'
        elif ten == 6:
            result += ' Sixty'
        elif ten == 7:
            result += ' Seventy'
        elif ten == 8:
            result += ' Eighty'
        elif ten == 9:
            result += ' Ninety'
        if one != 0:
            result += ' ' + self.digitToWord(one)
        return result.strip()

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        res = ''
        res += self.numberToWordsInThousand(num % 1000)
        num = num / 1000
        if num > 0:
            word = self.numberToWordsInThousand(num % 1000)
            if word:
                res = word + ' Thousand ' + res
        num = num / 1000
        if num > 0:
            word = self.numberToWordsInThousand(num % 1000)
            if word:
                res = word + ' Million ' + res
        num = num / 1000
        if num > 0:
            word = self.numberToWordsInThousand(num % 1000)
            if word:
                res = word + ' Billion ' + res
        return res.strip()


if __name__ == "__main__":
    print(Solution().numberToWords(1010))
    print(Solution().numberToWords(1234567))
