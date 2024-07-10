import io
from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        pointer = 0
        for log in logs:
            if log == '../':
                if pointer>0:
                    pointer-=1
            elif log =='./':
                continue
            else:
                pointer+=1
        return pointer

obj = Solution()
#data = obj.minOperations(logs = ["d1/","d2/","../","d21/","./"])
#data = obj.minOperations(logs = ["d1/","d2/","./","d3/","../","d31/"])
data = obj.minOperations(logs = ["d1/","../","../","../"])
print(data)