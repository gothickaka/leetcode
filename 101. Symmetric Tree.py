# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, p, q):
        if p == None and q == None:
            return True
        else:
            if p and q and p.val == q.val:
                return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left) and True
            else:
                return False

if __name__ == '__main__':
    s = Solution()
    list1 = TreeNode(0)
    list2 = TreeNode(1)
    list1.left = list2
    print(s.isSymmetric(list1))
