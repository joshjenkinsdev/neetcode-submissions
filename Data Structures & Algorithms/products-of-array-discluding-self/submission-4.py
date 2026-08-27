class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        
        prefix = 1
        for left in range(len(nums)):
            ans[left] = prefix
            prefix *= nums[left]
            
        suffix = 1
        for right in range(len(nums) - 1, -1, -1):
            ans[right] *= suffix
            suffix *= nums[right]
        
        return ans
            