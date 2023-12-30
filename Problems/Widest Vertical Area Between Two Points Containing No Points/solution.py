import io
from typing import List
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        n=len(points)
        ans=0
        for i in range(1,n):
            ans=max(ans,(points[i][0]-points[i-1][0]))
        return ans

obj = Solution()
#data = obj.maxWidthOfVerticalArea(points = [[8,7],[9,9],[7,4],[9,7]])
data = obj.maxWidthOfVerticalArea(points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])
print(data)