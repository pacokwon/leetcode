# Remove Nth Node From List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        tail = "<EMPTY>" if self.next is None else repr(self.next)
        return f"{self.val} - {tail}"

class Solution:
    def llLength(self, head):
        if head is None:
            return 0

        return self.llLength(head.next) + 1

    def removeNthFromEnd(self, head, n):
        length = self.llLength(head)
        target = length - n
        if target == 0:
            return head.next

        count = 0
        node = head
        while head is not None:
            if count == target - 1:
                node.next = node.next.next
                return head

            count += 1
            node = node.next

        # unreachable as long as test is valid
        return None

if __name__ == "__main__":
    sol = Solution()
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    node = ListNode(1)
    print(repr(sol.removeNthFromEnd(node, 1)))
