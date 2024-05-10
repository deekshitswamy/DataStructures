import io
from typing import List
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        ans=[0,1]
        left=0
        right=1
        while True:
            mid=(left+right)/2
            ans[0]=0
            count=0
            j=1
            for i in range(n):
                while j<n and arr[i]>mid*arr[j]:
                    j+=1
                count+=n-j
                if j==n:
                    break
                if ans[0]*arr[j]<ans[1]*arr[i]:
                    ans[0]=arr[i]
                    ans[1]=arr[j]
            if count<k:
                left=mid
            elif count>k:
                right=mid
            else:
                return ans

obj = Solution()
#data = obj.kthSmallestPrimeFraction(arr = [1,2,3,5], k = 3)
data = obj.kthSmallestPrimeFraction(arr = [1,7], k = 1)
print(data)