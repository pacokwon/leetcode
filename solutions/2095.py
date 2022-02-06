# Delete the Middle Node of a Linked List

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        tail = "<EMPTY>" if self.next is None else repr(self.next)
        return f"{self.val} - {tail}"

class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        if head is None:
            return 0

        return 1 + self.getLength(head.next)

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        if head.next is None:
            return None

        length = self.getLength(head)

        targetIndex = length // 2
        count = 0
        while True:
            # the node before the target
            if count == targetIndex - 1:
                ptr.next = ptr.next.next
                break

            count += 1
            ptr = ptr.next

        return head

if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1, ListNode(3,ListNode(4,ListNode(7, ListNode(1,ListNode(2,ListNode(6)))))))
    head = ListNode(1, ListNode(2,ListNode(3,ListNode(4))))
    head = ListNode(2, ListNode(1))
    head = ListNode(2)
    print( sol.deleteMiddle(head) )
