import io
from typing import List
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_l = list(map(int, version1.split(".")))
        v2_l = list(map(int, version2.split(".")))
        l1 = len(v1_l)
        l2 = len(v2_l)

        for i in range(max(l1, l2)):
            p1 = v1_l[i] if i<l1 else 0
            p2 = v2_l[i] if i<l2 else 0
            if p1 > p2:
                return 1
            elif p2 > p1:
                return -1
        
        return 0

obj = Solution()
#data = obj.compareVersion(version1 = "1.01", version2 = "1.001")
#data = obj.compareVersion(version1 = "1.0", version2 = "1.0.0")
data = obj.compareVersion(version1 = "0.1", version2 = "1.1")
print(data)