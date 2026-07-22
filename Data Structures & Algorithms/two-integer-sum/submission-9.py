class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, n in enumerate(nums):
            y = target - n
            if y in hash:
                return [hash[y], i]
            hash[n] = i