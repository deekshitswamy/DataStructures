import io
from typing import List
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count =0
        for j in range(low,high+1):
            s=str(j)
            n=len(s)
            if n%2==0:
                half = n//2
                left=s[:half]
                right=s[half:]
                sum1 = sum(int(c) for c in left)
                sum2 = sum(int(d) for d in right)
                if sum1==sum2:
                    count+=1
        return count

obj = Solution()
#data = obj.countSymmetricIntegers(low = 1, high = 100)
data = obj.countSymmetricIntegers(low = 1200, high = 1230)
print(data)