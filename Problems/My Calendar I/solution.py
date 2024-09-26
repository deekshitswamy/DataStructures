import io
from typing import List
class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        for b in self.booked:
            if max(b[0], start) < min(b[1], end):
                return False
        self.booked.append([start, end])
        return True

# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
obj = MyCalendar()
#data = obj.book(10, 20)
#data = obj.book(15, 25)
data = obj.book(20, 30)
print(data)