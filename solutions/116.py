# Populating Next Right Pointers in Each Node

# Definition for a Node.
class Node:
    def __init__(self, val = 0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def helper(self, root):
        if root is None:
            return [[], []]

        [ll, lr] = self.helper(root.left)
        [rl, rr] = self.helper(root.right)

        for l, r in zip(lr, rl):
            l.next = r

        ll.append(root)
        rr.append(root)

        return [ll, rr]

    def connect(self, root):
        self.helper(root)
        return root

if __name__ == "__main__":
    sol = Solution()
    node = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
