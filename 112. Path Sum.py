# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if not root: return False
        if not root.left and not root.right and root.val == sum: return True
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

if __name__ == '__main__':
    s = Solution()
    node1 = TreeNode(-2)
    node2 = TreeNode(3)
    node1.right = node2
    print(s.hasPathSum(node1,-2))
