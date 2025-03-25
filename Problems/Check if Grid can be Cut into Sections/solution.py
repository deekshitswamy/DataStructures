import io
from typing import List
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def helper(beg: int, end: int, cnt = 0) -> bool:

            order = sorted(range(m), key = lambda x: beg[x])
            acc = end[order.pop(0)]

            for i in order:
                if acc <= beg[i]: cnt+= 1
                if cnt >= 2: return True
                if acc <= end[i]: acc = end[i]
            return False

        m = len(rectangles)
        x_beg, y_beg, x_end, y_end  = map(list, zip(*rectangles))

        if helper(x_beg, x_end): return True
        return helper(y_beg, y_end)

obj = Solution()
#data = obj.checkValidCuts(n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]])
#data = obj.checkValidCuts(n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]])
data = obj.checkValidCuts(n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]])
print(data)