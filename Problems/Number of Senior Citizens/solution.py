import io
from typing import List
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for i in details:
            if int(i[11:13])>60: c+=1
        return c

obj = Solution()
#data = obj.countSeniors(details = ["7868190130M7522","5303914400F9211","9273338290F4010"])
data = obj.countSeniors(details = ["1313579440F2036","2921522980M5644"])
print(data)