import io
from typing import List
class MyCalendar:

    def __init__(self):
        pass
        

    def book(self, start: int, end: int) -> bool:
        pass

# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
obj = MyCalendar()
#data = obj.book(10, 20)
#data = obj.book(15, 25)
data = obj.book(20, 30)
print(data)