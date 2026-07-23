class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i, n in enumerate(nums):
            y = target - n
            if y in ans:
                return [ans[y], i]
            ans[n] = i