import io
from typing import List
class Solution:
    def largestOddNumber(self, num: str) -> str:
        i=len(num)-1
        while i>=0:
            check=int(num[i])
            if check%2!=0:
                return(num[:i+1])
                break
            else:
                num=num[:i]
            i-=1
        return("")

obj = Solution()
#data = obj.largestOddNumber(num = "52")
#data = obj.largestOddNumber(num = "4206")
data = obj.largestOddNumber(num = "35427")
print(data)