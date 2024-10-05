import io
from typing import List
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)):
            return False
        d1=defaultdict(int)
        d2=defaultdict(int)
        for i in s1:
            d1[i]+=1

        for i in range(len(s1)):
            d2[s2[i]]+=1
        
        if d1==d2:
            return True
        for i in range(len(s1),len(s2)):
            d2[s2[i]]+=1
            d2[s2[i-len(s1)]]-=1
            if d2[s2[i-len(s1)]]==0:
                del d2[s2[i-len(s1)]]
          
            if d1==d2:
                return True
        return False

obj = Solution()
#data = obj.checkInclusion(s1 = "ab", s2 = "eidbaooo")
data = obj.checkInclusion(s1 = "ab", s2 = "eidboaoo")
print(data)