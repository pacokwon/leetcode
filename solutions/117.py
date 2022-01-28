# Populating Next Right Pointers in Each Node II

# Definition for a Node.
class Node:
    def __init__(self, val = 0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
    def __repr__(self):
        left = "<EMPTY>" if self.left is None else f"{self.left.val}"
        right = "<EMPTY>" if self.right is None else f"{self.right.val}"
        return f"{self.val} - {left} - {right}"

class Solution:
    def helper(self, root):
        if root is None:
            return [], []

        ll, lr = self.helper(root.left)
        rl, rr = self.helper(root.right)

        if len(lr) < len(rl):
            diff = len(rl) - len(lr)
            for i in range(len(rl) - diff):
                lr[i].next = rl[i + diff]

            lr = rl[:diff] + lr
            ll = rl[:diff] + ll
        else:
            diff = len(lr) - len(rl)
            for i in range(len(lr) - diff):
                lr[i + diff].next = rl[i]

            rl = lr[:diff] + rl
            rr = lr[:diff] + rr

        ll.append(root)
        rr.append(root)

        return ll, rr

    def connect(self, root):
        self.helper(root)
        return root

# if __name__ == "__main__":
#     sol = Solution()
#     node = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))
#     node = Node(1, Node(2, Node(4), Node(5)), Node(3))
#     print(sol.connect(node).left.left.next)
