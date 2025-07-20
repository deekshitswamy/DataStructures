import io
from typing import List
class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        pass

obj = Solution()
#data = obj.deleteDuplicateFolder(paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]])
#data = obj.deleteDuplicateFolder(paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]])
data = obj.deleteDuplicateFolder(paths = [["a","b"],["c","d"],["c"],["a"]])
print(data)