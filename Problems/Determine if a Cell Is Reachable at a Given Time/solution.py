import io
from typing import List

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        ans=max(abs(sx-fx),abs(sy-fy))
        return t>=ans if ans else t!=1

obj = Solution()
#data = obj.isReachableAtTime(sx = 2, sy = 4, fx = 7, fy = 7, t = 6)
data = obj.isReachableAtTime(sx = 3, sy = 1, fx = 7, fy = 3, t = 3)
print(data)