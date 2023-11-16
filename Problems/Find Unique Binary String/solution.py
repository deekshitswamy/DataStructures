import io
from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        s=set(int(x,2) for x in nums)
        def pod(x,n):
            n1=len(x)
            return ("0"*(n-n1))+x
        for x in range(1<<n):
            if x not in s:
                return pod(bin(x)[2:],n)
        return "0"*n

obj = Solution()
#data = obj.findDifferentBinaryString(n = 1)
#data = obj.findDifferentBinaryString(n = 2)
data = obj.findDifferentBinaryString(n = 2)
print(data)