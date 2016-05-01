class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ret = []
        word_to_i = {word: i for i, word in enumerate(words)}
        for index, word in enumerate(words):
            if word[::-1] in word_to_i:
                rword_i = word_to_i[word[::-1]]
                if rword_i != index:
                    ret.append((rword_i, index))
                    ret.append((index, rword_i))
            for i in range(len(word) + 1):
                left = word[:i]
                right = word[i:]
                if self.is_palindrome(left) and right[::-1] in word_to_i:
                    ret.append((
                        word_to_i[right[::-1]],
                        index
                    ))
                if self.is_palindrome(right) and left[::-1] in word_to_i:
                    ret.append((
                        index,
                        word_to_i[left[::-1]]
                    ))
        return ret

    def is_palindrome(self, str):
        if not str:
            return False
        for i in range(len(str) / 2):
            if str[i] != str[len(str) - 1 - i]:
                return False
        return True


if __name__ == "__main__":
    print Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
