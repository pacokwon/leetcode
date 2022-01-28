# Remove Duplicates from Sorted List II

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        tail = "<EMPTY>" if self.next is None else repr(self.next)
        return f'{self.val} - {tail}'

class Solution:
    def deleteDuplicates(self, head):
        ptr = head
        curPtr = None
        newHead = None

        while ptr is not None:
            curVal = ptr.val

            hasDup = False
            while ptr.next is not None and ptr.next.val == curVal:
                hasDup = True
                ptr = ptr.next

            if hasDup:
                ptr = ptr.next
                continue

            next = ptr.next

            if curPtr is None:
                newHead = ptr
                curPtr = ptr
                curPtr.next = None
            else:
                curPtr.next = ptr
                curPtr = ptr
                curPtr.next = None

            ptr = next

        return newHead

if __name__ == "__main__":
    sol = Solution()
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
    node = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
    node = ListNode(1, ListNode(2, ListNode(2)))
    node = None
    # node = ListNode(1)
    print(sol.deleteDuplicates(node))
