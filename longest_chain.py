
def longestChain(words):
    """
    Find the longest word chain from words

    Args:
        words(list(str))

    Returns:
        int
    """
    def _dfs(word):
        """
        Do a dfs starting at word by removing a char from it.
        Update max length along the way
        """
        if word in memorization:
            return memorization[word]
        max_length = 1
        for i in range(len(word)):
            next_word = word[:i] + word[i + 1:]
            if next_word in word_set:
                next_word_length = _dfs(next_word)
                max_length = max(max_length, next_word_length + 1)
        memorization[word] = max_length
        return max_length

    word_set = set(words)
    max_length = 0
    memorization = {}
    for w in words:
        if len(w) < max_length:
            continue
        cur_length = _dfs(w)
        max_length = max(max_length, cur_length)
    return max_length


if __name__ == '__main__':
    print(longestChain(['a', 'b', 'ba', 'bca', 'bda', 'bdca']))
