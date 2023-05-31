# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the mid
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        
        # reverse the second half
        second = s.next
        prev = s.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            # second.next, s, second = s, second, second.next
            
        # merge LLs
        left, right = head, prev
        while left and right:
            temp1, temp2 = left.next, right.next
            left.next = right
            right.next = temp1
            left, right = temp1, temp2
    