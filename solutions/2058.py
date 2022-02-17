# Find the Minimum and Maximum Number of Nodes Between Critical Points

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]

        # ptr is not None, and ptr.next is not None
        ptr = head.next
        prev = head.val

        crits = []
        index = 1
        while ptr.next is not None:
            val = ptr.val
            next = ptr.next.val
            if prev < val and val > next:
                crits.append(index)
            if prev > val and val < next:
                crits.append(index)

            prev = val
            ptr = ptr.next
            index += 1

        if len(crits) < 2:
            return [-1, -1]

        maxDist = crits[-1] - crits[0]
        minDist = min(crits[index] - crits[index - 1] for index in range(1, len(crits)))

        return [minDist, maxDist]

if __name__ == "__main__":
    sol = Solution()
    head = ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))
    head = ListNode(3, ListNode(1))
    head = ListNode(2, ListNode(3, ListNode(3, ListNode(2))))
    print(sol.nodesBetweenCriticalPoints(head))
