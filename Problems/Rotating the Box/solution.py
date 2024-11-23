import io
from typing import List
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        pass

obj = Solution()
#data = obj.rotateTheBox(box = [["#",".","#"]])
#data = obj.rotateTheBox(box = [["#",".","*","."],["#","#","*","."]])
data = obj.rotateTheBox(box = [
    ["#","#","*",".","*","."],
    ["#","#","#","*",".","."],
    ["#","#","#",".","#","."]])
print(data)