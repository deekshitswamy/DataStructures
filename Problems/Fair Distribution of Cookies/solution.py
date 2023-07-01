import io
from typing import List
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if len(cookies) == k:
            return max(cookies)

        def backTrace(i, path):
            if i == len(cookies):
                return max(path)
            res = float('inf')
            for j in range(k):
                path[j] += cookies[i]
                res = min(res, backTrace(i+1, path))
                path[j] -= cookies[i]
            return res

        path = [0] * k
        return backTrace(0, path)


obj = Solution()
#data = obj.distributeCookies(cookies = [8,15,10,20,8], k = 2)
data = obj.distributeCookies(cookies = [6,1,3,2,2,4,1,2], k = 3)
print(data)