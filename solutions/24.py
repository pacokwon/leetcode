# Swap Nodes in Pairs

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        tail = "<EMPTY>" if self.next is None else repr(self.next)
        return f"{self.val} - {tail}"

class Solution:
    def swapPairs(self, head):
        # if list is empty or is of length 1, return it as it is
        if head is None or head.next is None:
            return head

        # now we can assume that there are at least two nodes in this list
        # swap head and head.next
        tail = head.next.next # we know that this is not None
        newHead = head.next
        newHead.next = head
        newHead.next.next = self.swapPairs(tail)
        return newHead

if __name__ == "__main__":
    sol = Solution()
    inp = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
    # inp = ListNode(1, None)
    # inp = ListNode(1, ListNode(2, None))
    print(repr(sol.swapPairs(inp)))
