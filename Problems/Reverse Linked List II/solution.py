import io

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if left == right:
            return head
        arr = []
        if not head or not head.next:
            return head
        temp = head
        i = 1
        while temp:
            if i == left:
                break
            i += 1
            temp = temp.next
        while temp:
            arr.append(temp.val)
            if i == right:
                break
            i += 1
            temp = temp.next
        temp = head
        i = 1
        while i != left:
            i += 1
            temp = temp.next
        while temp:
            temp.val = arr.pop()
            i += 1
            if i == right:
                temp.next.val = arr.pop()
                break
            temp = temp.next
        return head

obj = Solution()
#data = obj.reverseBetween(head = [1,2,3,4,5], left = 2, right = 4)
data = obj.reverseBetween(head = [5], left = 1, right = 1)
print(data)