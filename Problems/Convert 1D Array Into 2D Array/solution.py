import io
from typing import List
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if the total elements match m * n
        if n * m != len(original):
            return []
        
        ans = []
        temp = []
        cnt = 0
        
        for val in original:
            temp.append(val)  # Add the current element to the temp row
            cnt += 1
            
            if cnt == n:  # If temp has enough elements for one row
                ans.append(temp)  # Append the row to the 2D array
                temp = []  # Reset temp for the next row
                cnt = 0  # Reset the counter

        return ans

obj = Solution()
#data = obj.construct2DArray(original = [1,2,3,4], m = 2, n = 2)
#data = obj.construct2DArray(original = [1,2,3], m = 1, n = 3)
data = obj.construct2DArray(original = [1,2], m = 1, n = 1)
print(data)