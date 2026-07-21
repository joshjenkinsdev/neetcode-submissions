class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(i=0, cur=[], total=0):
            if total == target:
                ans.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return

            # include candidates[i]
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])
            cur.pop()

            # skip candidates[i]
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, cur, total)


        dfs()
        return ans