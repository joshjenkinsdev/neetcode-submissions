class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] + nums[fast] == target:
                break
            if fast == len(nums) - 1:
                slow += 1
                fast = slow + 1
            else:
                fast += 1
                
        return [slow, fast]