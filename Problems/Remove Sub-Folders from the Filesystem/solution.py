import io
from typing import List
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        pass

obj = Solution()
#data = obj.removeSubfolders(folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"])
#data = obj.removeSubfolders(folder = ["/a","/a/b/c","/a/b/d"])
data = obj.removeSubfolders(folder = ["/a/b/c","/a/b/ca","/a/b/d"])
print(data)