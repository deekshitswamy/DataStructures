import io
from typing import List
class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        ans=''
        for i,j in sorted(freq.items(),key=lambda x:x[1],reverse=True):
            ans=ans+i*j
        return ans

obj = Solution()
#data = obj.frequencySort(s = "tree")
#data = obj.frequencySort(s = "cccaaa")
data = obj.frequencySort(s = "Aabb")
print(data)