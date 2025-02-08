import io
from typing import List
class NumberContainers:

    def __init__(self):
        self.mpidx = {} 
        self.mpele = {}  

    def change(self, idx: int, ele: int) -> None:
        if idx in self.mpidx:
            old_ele = self.mpidx[idx]
            self.mpele[old_ele].remove(idx)
            if not self.mpele[old_ele]:
                del self.mpele[old_ele]

        self.mpidx[idx] = ele
        if ele not in self.mpele:
            self.mpele[ele] = SortedList()
        self.mpele[ele].add(idx)

    def find(self,ele: int) -> int:
        if ele in self.mpele and self.mpele[ele]:
            return self.mpele[ele][0]
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
obj = NumberContainers()
# obj.change(["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
# [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]])
# param_2 = obj.find(number)

# obj = Solution()
# #data = obj.testfunc(n = 1)
# #data = obj.testfunc(n = 2)
# data = obj.testfunc(n = 2)
# print(data)