import io
from typing import List
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = [0] * 30

        for i in candidates:
            for j in range(30):
                if i & (1 << j):
                    res[j] += 1

        max_count = max(res)
        return max_count

obj = Solution()
#data = obj.largestCombination(candidates = [16,17,71,62,12,24,14])
data = obj.largestCombination(candidates = [8,8])
print(data)