class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 2^n = num of subsets
        ans = []
        
        # use dfs backtracking
        subset = []
        def dfs(i):
            if i >= len(nums):
                ans.append(subset.copy())
                return
            
            # include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # don't include nums[i]
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return ans
            
            
            