import io
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash={}

        for i in range (len(arr)):
            if arr[i] not in hash:    
                hash[arr[i]]=1
            else:
                hash[arr[i]]=hash[arr[i]]+1
        
        return len(set(hash.values()))== len(hash.values())

obj = Solution()
#data = obj.uniqueOccurrences(arr = [1,2,2,1,1,3])
#data = obj.uniqueOccurrences(arr = [1,2])
data = obj.uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0])
print(data)