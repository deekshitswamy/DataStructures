import io
from typing import List
class CustomStack:

    def __init__(self, maxSize: int):
        pass
        

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def increment(self, k: int, val: int) -> None:
        pass


# Your CustomStack object will be instantiated and called as such:
stk =  CustomStack(3); 
stk.push(1);                          
stk.push(2);                           
stk.pop();                            
stk.push(2);                           
stk.push(3);                            
stk.push(4);                            
stk.increment(5, 100);                 
stk.increment(2, 100);                 
stk.pop();                             
stk.pop();                             
stk.pop();                             
stk.pop();                             