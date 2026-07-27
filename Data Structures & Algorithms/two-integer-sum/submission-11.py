class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i
        
        for ind, num in enumerate(nums):
            diff = target - num
            if diff in indices and indices[diff] != ind:
                return [ind, indices[diff]]
        return []