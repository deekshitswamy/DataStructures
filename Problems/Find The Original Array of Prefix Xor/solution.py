import io
from typing import List
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref)==1:
            return pref
        ans=[pref[0]]
        for i in range(len(pref)-1):
            ans.append(pref[i]^pref[i+1])
        return ans

obj = Solution()
#data = obj.findArray(pref = [5,2,0,3,1])
data = obj.findArray(pref = [13])
print(data)