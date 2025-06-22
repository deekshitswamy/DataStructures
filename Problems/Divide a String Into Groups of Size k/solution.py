import io
from typing import List
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        output = []
        for i in range(0, len(s), k):
            if i <= len(s)-k:
                output.append(s[i:i+k])
            else:
                s += fill * (k - (len(s) % k))
                output.append(s[i:])
        return output

obj = Solution()
#data = obj.divideString(s = "abcdefghi", k = 3, fill = "x")
data = obj.divideString(s = "abcdefghij", k = 3, fill = "x")
print(data)