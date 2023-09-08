import io
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        #building the rows to append
        for i in range(numRows - 1):
		    #padding the temp array to make computation easier
            temp = [0] + result[-1] + [0]
            row = []
            #building the rows
            for j in range(len(temp) - 1):
                row.append(temp[j] + temp[j + 1])
            result.append(row)
        return result

obj = Solution()
#data = obj.generate(numRows = 5)
data = obj.generate(numRows = 1)
print(data)