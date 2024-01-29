import io
from typing import List
class MyQueue:

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)    
        while self.s2:
            self.s1.append(self.s2.pop())


    def pop(self) -> int:
        return self.s1.pop()


    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1


# Your MyQueue object will be instantiated and called as such:
input_command = ["MyQueue", "push", "push", "peek", "pop", "empty"]
data = [[], [1], [2], [], [], []]

#myQueue = MyQueue()
#myQueue.push(1) # queue is: [1]
#myQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)
#myQueue.peek() # return 1
#myQueue.pop() # return 1, queue is [2]
#myQueue.empty() # return false