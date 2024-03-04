import io
from typing import List
from collections import deque
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        q=deque(sorted(tokens))
        cur=0
        ans=0
        while q:
            if q[0]<=power:
                power-=q.popleft()
                cur+=1
                ans=max(cur,ans)

            elif cur>0:
                power+=q.pop()
                cur-=1

            else:
                break
        return ans

obj = Solution()
#data = obj.bagOfTokensScore(tokens = [100], power = 50)
#data = obj.bagOfTokensScore(tokens = [200,100], power = 150)
data = obj.bagOfTokensScore(tokens = [100,200,300,400], power = 200)
print(data)