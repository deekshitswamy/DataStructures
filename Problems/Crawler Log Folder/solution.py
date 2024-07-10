import io
from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        pass

obj = Solution()
#data = obj.minOperations(logs = ["d1/","d2/","../","d21/","./"])
#data = obj.minOperations(logs = ["d1/","d2/","./","d3/","../","d31/"])
data = obj.minOperations(logs = ["d1/","../","../","../"])
print(data)