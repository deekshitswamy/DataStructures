import io
from typing import List
from collections import Counter
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        c = Counter()
        for line in grid:
            c.update(line)
        
        if len({key % x for key in c}) > 1:
            return -1
        
        data = sorted((k // x, v) for k, v in c.items())

        left_sum = left_cnt = 0
        right_sum = sum(k * v for k, v in data)
        right_cnt = len(grid) * len(grid[0])

        result = float('inf')
        for i, (k, v) in enumerate(data):
            right_cnt -= v
            right_sum -= k * v
            result = min(
                result,
                right_sum - left_sum + k * (left_cnt - right_cnt),
            )
            left_cnt += v
            left_sum += k * v
        return result

obj = Solution()
#data = obj.minOperations(grid = [[2,4],[6,8]], x = 2)
#data = obj.minOperations(grid = [[1,5],[2,3]], x = 1)
data = obj.minOperations(grid = [[1,2],[3,4]], x = 2)
print(data)