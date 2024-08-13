import io
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, curr = [], []
        n = len(candidates)
        candidates.sort()

        def backtrack(index, total):
            if total == target:
                res.append(curr.copy())
            if total >= target or index == n:
                return
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                backtrack(i + 1, total + candidates[i])
                curr.pop()
        
        backtrack(0, 0)
        return res

obj = Solution()
#data = obj.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)
data = obj.combinationSum2(candidates = [2,5,2,1,2], target = 5)
print(data)