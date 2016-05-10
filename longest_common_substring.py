

def longest_common_substring(a, b):
    if not a or not b:
        return 0

    # dp[i][j] denotes the length of the common suffix of a[:i] and b[:j]
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    global_max = 0

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0
            global_max = max(global_max, dp[i][j])
    return global_max


if __name__ == '__main__':
    print(longest_common_substring('bdabcd', 'aababca'))
    print(longest_common_substring('people', 'apples'))
