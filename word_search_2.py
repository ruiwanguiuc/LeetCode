
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True

    def search(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.is_end


class Solution(object):

    def dfs(self, board, i, j, word, trie_node):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) \
                or board[i][j] not in trie_node.children:
            return []
        next_node = trie_node.children[board[i][j]]
        all_words = []
        if next_node.is_end:
            all_words.append(word + board[i][j])
        tmp = board[i][j]
        board[i][j] = '#'
        for found in self.dfs(board, i - 1, j, word + tmp, next_node):
            all_words.append(found)
        for found in self.dfs(board, i + 1, j, word + tmp, next_node):
            all_words.append(found)
        for found in self.dfs(board, i, j - 1, word + tmp, next_node):
            all_words.append(found)
        for found in self.dfs(board, i, j + 1, word + tmp, next_node):
            all_words.append(found)
        board[i][j] = tmp
        return all_words

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not words or not board or not board[0]:
            return []
        root = TrieNode()
        for word in words:
            root.insert(word)

        all_words = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                for found_word in self.dfs(board, i, j, '', root):
                    all_words.add(found_word)
        return list(all_words)


if __name__ == "__main__":
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    # board = [['a']]
    # words = ['a']
    print Solution().findWords(board, words)
