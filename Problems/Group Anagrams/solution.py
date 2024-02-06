import io
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp  = {}
        for i in range(len(strs)):
            string = strs[i]
            new = " ".join(sorted(string))
            
            if new not in mp:
                mp[new] = [string]
            else:
                mp[new].append(string)

        ans = []
        for j in mp:
            ans.append(mp[j])
        
        return ans

obj = Solution()
#data = obj.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])
#data = obj.groupAnagrams(strs = [""])
data = obj.groupAnagrams(strs = ["a"])
print(data)