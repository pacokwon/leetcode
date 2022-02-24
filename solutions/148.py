from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        tail = "<EMPTY>" if self.next is None else repr(self.next)
        return f"{self.val} - {tail}"

class Solution:
    def fillArr(self, head: Optional[ListNode], lst: List[int]):
        if head is None:
            return

        lst.append(head.val)
        self.fillArr(head.next, lst)

    def toList(self, lst: List[int], index=0) -> Optional[ListNode]:
        if index >= len(lst):
            return None

        return ListNode(lst[index], self.toList(lst, index + 1))

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        lst = []
        self.fillArr(head, lst)
        lst.sort()
        return self.toList(lst)

if __name__ == "__main__":
    sol = Solution()
    head = ListNode(-1,ListNode(5,ListNode(3,ListNode(4,ListNode(0)))))
    print(repr(sol.sortList(head)))
