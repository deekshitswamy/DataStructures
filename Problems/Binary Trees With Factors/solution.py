import io
from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod=10**9+7
        arr.sort()
        ans=defaultdict(int)
        for a in arr:
            tmp=1
            for b in arr:
                if b>a:
                    break
                tmp+=(ans[b]*ans[a/b])
            ans[a]=tmp
        return sum(ans.values())%mod 

obj = Solution()
#data = obj.numFactoredBinaryTrees(arr = [2,4])
data = obj.numFactoredBinaryTrees(arr = [2,4,5,10])
print(data)