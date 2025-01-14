import io
from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = [0]*len(A)
        seen = set()
        count= 0

        for i in range(len(A)):
            if A[i] in seen:
                count+=1
            seen.add(A[i])
            if B[i] in seen:
                count+=1
            seen.add(B[i])

            C[i] = count
        
        return C

obj = Solution()
#data = obj.findThePrefixCommonArray(A = [1,3,2,4], B = [3,1,2,4])
data = obj.findThePrefixCommonArray(A = [2,3,1], B = [3,1,2])
print(data)