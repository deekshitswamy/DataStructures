import io
from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ans=0
        while len(students)>ans:
            if students[0]==sandwiches[0]:
                sandwiches.pop(0)
                ans=0
            else:
                students.append(students[0])
                ans+=1
            students.pop(0)
        return len(students)

obj = Solution()
#data = obj.countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1])
data = obj.countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1])
print(data)