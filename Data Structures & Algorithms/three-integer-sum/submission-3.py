class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(0, len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    curr = sorted([nums[i], nums[j], nums[k]])
                    exists = False
                    for a in ans:
                        if a == curr:
                            exists = True
                    if not exists:
                        ans.append(curr)
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return ans