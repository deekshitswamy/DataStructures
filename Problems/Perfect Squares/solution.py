import io
from typing import List
class Solution:
    def numSquares(self, n: int) -> int:
        q = deque()
        sqrs = [i*i for i in range(1, int(n ** 0.5) + 1)][::-1]
        q.append((n, 0))
        vis = set()

        while q:
            p, step = q.popleft()
            if p == 0:
                return step
            for sq in sqrs:
                if (p - sq) >= 0 and (p - sq) not in vis:
                    q.append((p - sq, step + 1))
                    vis.add(p - sq)
        return 0

obj = Solution()
#data = obj.numSquares(n = 12)
data = obj.numSquares(n = 13)
print(data)