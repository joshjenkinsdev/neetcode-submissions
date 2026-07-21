class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        
        # use dfs backtracking
        subset = []
        def dfs(i, total):
            # if total is equal, return
            if total == target:
                ans.append(subset.copy())
                return
            # i cannot be greater than length of array
            if i >= len(nums) or total > target:
                return
                
            # if total is smaller, append, we need more
            subset.append(nums[i])
            dfs(i, total + nums[i])
            subset.pop()

            dfs(i + 1, total)
            
        dfs(0, 0)
        return ans