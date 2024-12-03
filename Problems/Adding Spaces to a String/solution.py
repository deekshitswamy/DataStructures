import io
from typing import List
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = [''] * (len(s) + len(spaces))
        write_pos = 0
        read_pos = 0
        
        for space_pos in spaces:
            while read_pos < space_pos:
                result[write_pos] = s[read_pos]
                write_pos += 1
                read_pos += 1
            result[write_pos] = ' '
            write_pos += 1
            
        while read_pos < len(s):
            result[write_pos] = s[read_pos]
            write_pos += 1
            read_pos += 1
            
        return ''.join(result)

obj = Solution()
#data = obj.addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15])
#data = obj.addSpaces(s = "icodeinpython", spaces = [1,5,7,9])
data = obj.addSpaces(s = "spacing", spaces = [0,1,2,3,4,5,6])
print(data)