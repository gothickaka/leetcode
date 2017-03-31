# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

if __name__ == '__main__':
    s = Solution()
    node1 = TreeNode(-2)
    node2 = TreeNode(3)
    node3 = TreeNode(5)
    node1.left = node2
    node2.right = node3
    print(s.isBalanced(node1))
