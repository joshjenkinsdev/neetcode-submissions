class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans, prefixes, suffixes, = [0] * n, [0] * n, [0] * n
        prefixes[0] = suffixes[n - 1] = 1

        for i in range(1, n):
            prefixes[i] = nums[i - 1] * prefixes[i - 1]
        for j in range(n - 2, -1, -1):
            suffixes[j] = nums[j + 1] * suffixes[j + 1]
        for k in range(n):
            ans[k] = prefixes[k] * suffixes[k]
        return ans
