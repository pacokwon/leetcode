# Maximum Twin Sum of a Linked List

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def toList(self, head: Optional[ListNode]) -> List[int]:
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next
        return l

    def pairSum(self, head: Optional[ListNode]) -> int:
        l = self.toList(head)
        length = len(l)

        ans = l[0] + l[-1]
        for i in range(1, length // 2):
            ans = max(ans, l[i] + l[length - 1 - i])
        return ans
