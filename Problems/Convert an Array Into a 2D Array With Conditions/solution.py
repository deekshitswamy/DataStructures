import io
from typing import List
from collections import Counter
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        count=Counter(nums)
        while count:
            val=[]
            drop=[]
            for k,v in count.items():
                val.append(k)
                count[k]-=1
                if count[k]==0:
                    drop.append(k)

            for k in drop:
                count.pop(k)

            ans.append(val)

        return ans

obj = Solution()
#data = obj.findMatrix(nums = [1,3,4,1,2,3,1])
data = obj.findMatrix(nums = [1,2,3,4])
print(data)