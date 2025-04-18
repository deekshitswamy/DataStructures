import io
from typing import List
class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(n-1):
            temp = ""
            count = 1
            for i in range(1, len(res)):
                if res[i] == res[i-1]:
                    count += 1
                else :
                    temp += str(count) + res[i-1]
                    count = 1
            temp += str(count) + res[-1]
            res = temp
        return res

obj = Solution()
#data = obj.countAndSay(n = 1)
data = obj.countAndSay(n = 4)
print(data)