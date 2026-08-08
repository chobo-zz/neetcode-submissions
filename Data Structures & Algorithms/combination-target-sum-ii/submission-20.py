class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, cur, remaining):
            if remaining == 0:
                res.append(cur.copy())
                return
            
            if i >= len(candidates) or remaining < 0:
                return
            
            cur.append(candidates[i])
            dfs(i + 1, cur, remaining - candidates[i])

            cur.pop()
            while (i + 1) < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, cur, remaining)
        
        dfs(0, [], target)
        return res