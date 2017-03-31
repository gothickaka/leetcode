# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1
        elif not root.left and not root.right:
            return 1
        return self.minDepth(root.left)+self.minDepth(root.right)+1

if __name__ == '__main__':
    s = Solution()
    node1 = TreeNode(-2)
    node2 = TreeNode(3)
    node3 = TreeNode(5)
    node1.left = node2
    node2.right = node3
    print(s.minDepth(node1))
