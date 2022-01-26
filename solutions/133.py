# Clone Graph

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"{self.val} - [{', '.join(str(n.val) for n in self.neighbors)}]"

class Solution:
    def cloneHelper(self, node, nodeMap):
        newNode = Node(node.val, None)
        nodeMap[newNode.val] = newNode

        neighbors = [None] * len(node.neighbors)
        for index, neighbor in enumerate(node.neighbors):
            if neighbor.val in nodeMap:
                neighbors[index] = nodeMap[neighbor.val]
            else:
                neighbors[index] = self.cloneHelper(neighbor, nodeMap)

        newNode.neighbors = neighbors
        return newNode

    def cloneGraph(self, node):
        nodes = {}
        if node is None:
            return None

        return self.cloneHelper(node, nodes)

if __name__ == "__main__":
    sol = Solution()
    three = Node(3, [])
    inp = Node(1, [Node(2, [three]), three])
    print(sol.cloneGraph(inp))
