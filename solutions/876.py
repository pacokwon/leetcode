# Middle Of The Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def llLength(self, head):
        if head is None:
            return 0

        return 1 + self.llLength(head.next)

    def middleNode(self, head):
        length = self.llLength(head)
        midLength = length // 2 + 1

        count = 0
        while True:
            count += 1
            if count == midLength:
                return head

            head = head.next

if __name__ == "__main__":
    sol = Solution()
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
