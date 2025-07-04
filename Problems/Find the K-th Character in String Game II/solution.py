import io
from typing import List
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        lengths = [1]
        for op in operations:
            lengths.append(lengths[-1] * 2)
        
        shift = 0
        for i in reversed(range(len(operations))):
            half = lengths[i]
            if k > half:
                k -= half
                if operations[i] == 1:
                    shift = (shift + 1) % 26
        return chr((shift % 26) + ord('a'))

obj = Solution()
#data = obj.kthCharacter(k = 5, operations = [0,0,0])
data = obj.kthCharacter(k = 10, operations = [0,1,0,1])
print(data)