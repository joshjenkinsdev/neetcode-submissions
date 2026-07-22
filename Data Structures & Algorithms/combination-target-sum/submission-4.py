class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        def dfs(i, total):
            if total == target:
                ans.append(subset.copy())
                return
            elif i >= len(nums) or total >= target:
                return
            
            #include
            subset.append(nums[i])
            dfs(i, total + nums[i])

            #exclude
            subset.pop()
            dfs(i+1, total)
        
        dfs(0,0)

        return ans