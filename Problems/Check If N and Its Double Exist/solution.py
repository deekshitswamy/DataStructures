import io
from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] * 2 == arr[j] or arr[i] == 2 * arr[j]:
                    return True
        return False

obj = Solution()
#data = obj.checkIfExist(arr = [10,2,5,3])
data = obj.checkIfExist(arr = [3,1,7,11])
print(data)