import io
from typing import List
from collections import defaultdict
class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        for i, j in enumerate(conflictingPairs):
            [a, b] = j
            if a > b:
                conflictingPairs[i] = [b, a]

        conflictingPairs = sorted(conflictingPairs, key=lambda x: (x[1], x[0]))
        ln = len(conflictingPairs)
        hel = [0 for _ in range(ln)]
        pairs = 0
        d = defaultdict(list)
        for index, i in enumerate(conflictingPairs):
            [a, b] = i
            d[a].append([b, index])
        last = n + 1
        next_last = n + 1
        dc = defaultdict(list)
        for i in range(n, 0, -1):
            for j in d[i]:
                [end, index] = j
                dc[end].append(index)
                if end < last:
                    next_last = last
                    last = end
                elif end < next_last:
                    next_last = end
            pairs += last - i
            diff = (next_last - last)
            index = dc[last][0] if len(dc[last]) == 1 else -1
            if index == -1:
                continue
            hel[index] += diff
        return pairs + max(hel)

obj = Solution()
#data = obj.maxSubarrays(n = 4, conflictingPairs = [[2,3],[1,4]])
data = obj.maxSubarrays(n = 5, conflictingPairs = [[1,2],[2,5],[3,5]])
print(data)