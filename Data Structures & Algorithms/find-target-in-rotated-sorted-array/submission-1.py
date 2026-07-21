class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # if found
            if target == nums[mid]:
                return mid
            
            # might be left since it's less than mid, so let's check
            if nums[left] <= nums[mid]:
                # move right if target is GREATER than mid OR is LESS than the leftmost value (must be rotated)
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                # otherwise, move left
                else:
                    right = mid - 1

            else:
                # move left if target is LESS than mid OR is GREATER than the rightmost value (must be rotated)
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                # otherwise move right 
                else:
                    left = mid + 1
            
        return -1
            
        