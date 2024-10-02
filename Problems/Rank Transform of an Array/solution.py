import io
from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        value_to_rank = {}  # Dictionary to store value-to-rank mapping
        sorted_unique_numbers = sorted(list(set(arr)))  # Remove duplicates and sort unique elements
        
        # Assign ranks to sorted unique elements
        for index in range(len(sorted_unique_numbers)): 
            value_to_rank[sorted_unique_numbers[index]] = index + 1
          
        # Replace each element in the original array with its rank
        for index in range(len(arr)): 
            arr[index] = value_to_rank[arr[index]]
        
        return arr  # Return the updated array

obj = Solution()
#data = obj.arrayRankTransform(arr = [40,10,20,30])
#data = obj.arrayRankTransform(arr = [100,100,100])
data = obj.arrayRankTransform(arr = [37,12,28,9,100,56,80,5,12])
print(data)