import io
from typing import List
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        N = len(heights)
        jumps = []
        bricks_used = 0

        for i in range(N-1):
            if heights[i] < heights[i+1]:
                diff = heights[i+1] - heights[i]
                if len(jumps) < ladders:
                    heappush(jumps, diff)
                else:
                    if ladders > 0 and jumps[0] < diff:
                        bricks_used += heappop(jumps)
                        heappush(jumps, diff)
                    else:
                        bricks_used += diff
                    if bricks_used > bricks:
                        return i
            
        return N-1

obj = Solution()
#data = obj.furthestBuilding(heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1)
#data = obj.furthestBuilding(heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2)
data = obj.furthestBuilding(heights = [14,3,19,3], bricks = 17, ladders = 0)
print(data)