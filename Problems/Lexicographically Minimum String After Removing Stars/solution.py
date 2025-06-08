import io
from typing import List
from heapq import heappop, heappush
class Solution:
    def clearStars(self, s: str) -> str:
        heap=[]
        for i, c in enumerate(s):
            if c=='*':
                heappop(heap)
            else:
                heappush(heap,(c,-i))
        ans = ['']*len(s)
        while heap:
            char, i=heappop(heap)
            ans[-i]=char

        return ''.join(ans)

obj = Solution()
#data = obj.clearStars(s = "aaba*")
data = obj.clearStars(s = "abc")
print(data)