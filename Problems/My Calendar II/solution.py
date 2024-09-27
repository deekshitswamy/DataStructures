import io
from typing import List
class MyCalendarTwo:

    def __init__(self):
        self.cal = []
        self.intrscs = []

    def book(self, start: int, end: int) -> bool:
        for x in self.intrscs:
            if (start < x[0] and end > x[0]) or (start >= x[0] and start < x[1]):
                return False

        for x in self.cal:
            if (start < x[0] and end > x[0]) or (start >= x[0] and start < x[1]):
                cs = max(x[0], start)
                ce = min(x[1], end)
                self.intrscs.append([cs, ce])

        self.cal.append([start, end])
        return True

obj = MyCalendarTwo()
#data = obj.book(10, 20)
#data = obj.book(50, 60)
data = obj.book(10, 40)
print(data)