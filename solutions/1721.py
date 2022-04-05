from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        tail = "<EMPTY>" if self.next is None else repr(self.next)
        return f"{self.val} - {tail}"

def toList(arr):
    if not arr:
        return None

    return ListNode(arr[0], toList(arr[1:]))

class Solution:
    def length(self, head: Optional[ListNode]) -> int:
        if head is None:
            return 0

        return 1 + self.length(head.next)

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # can't do anything
        if head is None or head.next is None:
            return head

        length = self.length(head)
        if k > length // 2:
            k = length + 1 - k

        # swap the head and the tail.
        # this is handled separately since the head changes
        if k == 1:
            # length is two
            if head.next.next is None:
                ptr = head.next
                ptr.next = head
                head.next = None
                return ptr

            beforeTail = head
            while beforeTail.next.next is not None:
                beforeTail = beforeTail.next
            tail = beforeTail.next
            tail.next = head.next
            head.next = None
            beforeTail.next = head
            return tail

        curr = head
        prev = None
        count = 0

        kNode = None
        kNodePrev = None

        while curr.next is not None:
            count += 1
            if count == k:
                kNode = curr
                kNodePrev = prev
                print(kNode.val)
                print(kNodePrev.val)

            elif count == length + 1 - k:
                # swapping nodes are adjacent.
                if k + 1 == length + 1 - k:
                    next = curr.next
                    kNodePrev.next = curr
                    curr.next = kNode
                    kNode.next = next
                    break
                next = curr.next

                kNodePrev.next = curr
                curr.next = kNode.next

                prev.next = kNode
                kNode.next = next

                break

            prev = curr
            curr = curr.next

        return head

# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# head = ListNode(1, ListNode(2))

# head = toList([7,9,6,6,7,8,3,0,9,5])
# k = 5
# head = toList([80,46,66,35,64])
# k = 1
# print(repr(Solution().swapNodes(head, k)))
