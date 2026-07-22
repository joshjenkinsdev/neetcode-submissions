class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(0, len(nums)-2):
            left, right = i + 1, len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    curr = sorted([nums[i], nums[left], nums[right]])
                    exists = False
                    for a in ans:
                        if curr == a:
                            exists = True
                    if not exists:
                        ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return ans
