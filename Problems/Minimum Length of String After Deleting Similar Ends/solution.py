import io
import collections
from typing import List
class Solution:
    def minimumLength(self, s: str) -> int:
        ans=collections.deque(s)
        while len(ans)>1 and ans[0]==ans[-1]:
            cur=ans[0]
            while len(ans)>0 and ans[0]==cur:
                ans.popleft()
            while len(ans)>0 and ans[-1]==cur:
                ans.pop()
        return len(ans)

obj = Solution()
#data = obj.minimumLength(s = "ca")
#data = obj.minimumLength(s = "cabaabac")
data = obj.minimumLength(s = "aabccabba")
print(data)