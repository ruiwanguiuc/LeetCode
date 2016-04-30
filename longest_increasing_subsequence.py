
def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    lis_all = 1
    lis_ending_here = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i - 1, -1, -1):
            if nums[j] < nums[i]:
                lis_ending_here[i] = lis_ending_here[j] + 1
                break
        lis_all = max(lis_all, lis_ending_here[i])
    return lis_all


if __name__ == "__main__":
    print(lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
