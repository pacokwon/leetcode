# Merge k Sorted Lists

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        tail = "<EMPTY>" if self.next is None else repr(self.next)
        return f"{self.val} - {tail}"

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        if list1.val < list2.val:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        else:
            return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length = len(lists)
        if length == 0:
            return None

        while length != 1:
            left, right = 0, length - 1
            while left < right:
                lists[left] = self.mergeTwoLists(lists[left], lists[right])
                left += 1
                right -= 1
            length = (length + 1) // 2
        return lists[0]

if __name__ == "__main__":
    sol = Solution()
    lists = [[1,4,5],[1,3,4],[2,6]]
    lists = [ListNode(1,ListNode(4,ListNode(5))),ListNode(1,ListNode(3,ListNode(4))),ListNode(2,ListNode(6))]
    lists = []
    lists = [None]
    print(repr(sol.mergeKLists(lists)))
