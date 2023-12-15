import io
from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        frm,to=zip(*paths)
        return (set(to)-set(frm)).pop()

obj = Solution()
#data = obj.destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
#data = obj.destCity(paths = [["B","C"],["D","B"],["C","A"]])
data = obj.destCity(paths = [["A","Z"]])
print(data)