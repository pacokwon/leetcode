# Add Two Numbers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printListNode(self, l):
        while l is not None:
            print(l.val, end='')
            l = l.next
        print()

    def toNum(self, l):
        nums = []
        while l is not None:
            nums.append(str(l.val))
            l = l.next

        return int(''.join(reversed(nums)))

    def toListNode(self, num):
        s = str(num)
        ln = ListNode(s[0], None)

        for c in s[1:]:
            ln = ListNode(c, ln)

        return ln

    def addTwoNumbers(self, l1, l2):
        n1 = self.toNum(l1)
        n2 = self.toNum(l2)
        return self.toListNode(n1 + n2)

if __name__ == "__main__":
    sol = Solution()
    l1 = sol.toListNode(9999999)
    l2 = sol.toListNode(9999)
    sol.printListNode(sol.addTwoNumbers(l1, l2))
