# Reverse Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        tail = "<EMPTY>" if self.next is None else repr(self.next)
        return f"{self.val} - {tail}"

class Solution:
    def helper(self, head):
        if head.next.next is None:
            # node1 -> node2 -> NULL
            newHead = head.next
            newTail = head
            newHead.next = newTail
            newTail.next = None

            return newHead, newTail

        newHead, newTail = self.helper(head.next)
        newTail.next = head
        head.next = None
        return newHead, head

    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        newHead, _ = self.helper(head)
        return newHead


if __name__ == "__main__":
    sol = Solution()
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # node = ListNode(1, ListNode(2, ListNode(3)))
    print(repr(sol.reverseList(node)))
