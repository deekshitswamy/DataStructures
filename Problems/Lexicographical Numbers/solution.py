import io
from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        number = {}
        s = str(n)
        length = len(s) 
        for i in range(1, n + 1):
            number[i] = i * (10 ** (length - len(str(i))))
        d = sorted(number.items(), key=lambda number: number[1])
        result = []
        for key, value in d:
            result.append(key)
        return result

obj = Solution()
#data = obj.lexicalOrder(n = 13)
data = obj.lexicalOrder(n = 2)
print(data)